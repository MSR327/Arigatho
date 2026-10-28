import pytest

from oa.common import append_jsonl, read_jsonl
from oa.sort import (ClaudeError, UsageLimit, apply_duplicates, build_batch_prompt, dedupe, dedupe_pending,
                     format_message, is_sortable, normalize_rows, sort_pending, to_questions)
from oa.store import Archive


def rec(i, text="", att=None, reply=None, deleted=False):
    return {"id": i, "group": "inter-iit", "sent_at": "2026-10-14T21:52:01+00:00", "text": text,
            "author_tag": "IITD", "reply_to": reply, "attachment": att, "deleted": deleted}


PDF = {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 10, "is_image": False}
REPLY = {"id": 6808, "text": "I want rystad Energy oa questions?", "author_tag": "NITR"}


def share(**kw):
    s = {"company": "Rystad Energy", "college": "IIT Delhi", "date": "2026-10-14", "role": "fte",
         "source_ids": [6827], "questions": [{"title": "Max subarray", "text": "Given...",
                                              "topics": ["Arrays", "DP"]}]}
    s.update(kw)
    return s


def test_format_message_has_context_and_file():
    line = format_message(rec(6827, att=PDF, reply=REPLY))
    assert "[6827] 2026-10-14 IITD" in line
    assert 'reply to [6808] (NITR): "I want rystad Energy oa questions?"' in line
    assert "archive/files/6827-rystad_1_.pdf (application/pdf)" in line


def test_build_batch_prompt_lists_messages_topics_companies():
    p = build_batch_prompt([rec(1, "Amazon OA today")], ["Amazon", "Google"])
    assert "[1] 2026-10-14 IITD" in p and "Amazon OA today" in p
    assert "Sliding Window" in p and "Amazon, Google" in p


def test_is_sortable():
    assert is_sortable(rec(1, "hi"))
    assert is_sortable(rec(1, att=PDF))
    assert not is_sortable(rec(1, ""))
    assert not is_sortable(rec(1, "x", deleted=True))


def test_to_questions_valid():
    rows = to_questions([share(), share(questions=[{"title": "A", "text": "a", "topics": ["SQL"]},
                                                   {"title": "B", "text": "b", "topics": ["Math"]}])],
                        {6827})
    assert [r["qid"] for r in rows] == ["6827-1", "6827-2", "6827-3"]
    assert rows[0]["company"] == "Rystad Energy" and rows[0]["duplicate_of"] is None


@pytest.mark.parametrize("bad", [
    share(source_ids=[999]),                       # not in this batch
    share(date="14 Oct"),                          # bad date
    share(role="sde"),                             # bad role
    share(company=" "),                            # empty company
    share(questions=[{"title": "A", "text": "a", "topics": ["Cooking"]}]),  # unknown topic
])
def test_to_questions_rejects(bad):
    with pytest.raises(ValueError):
        to_questions([bad], {6827})


def test_sort_pending_batches_retries_and_skips(tmp_path):
    a = Archive(tmp_path / "archive")
    a.add([rec(1, "Amazon OA: two sum"), rec(2, ""), rec(3, "Google OA"), rec(4, "chat")])
    state = {"groups": {}, "sorted_ids": []}
    calls = []

    def runner(prompt, schema):
        calls.append(prompt)
        if "[1]" in prompt:
            return {"shares": [share(company="Amazon", source_ids=[1])]}
        if len(calls) == 2:
            raise ClaudeError("flaky")
        return {"shares": []}

    qpath = tmp_path / "q.jsonl"
    rows = sort_pending(a, state, runner=runner, batch_size=1, questions_path=qpath)
    assert [r["company"] for r in rows] == ["Amazon"]
    assert sorted(state["sorted_ids"]) == [1, 2, 3, 4]  # 2 is empty: marked sorted without a call
    assert len(calls) == 4  # 1, 3 (fail), 3 (retry), 4
    assert qpath.read_text().count('"Amazon"') == 1


def test_sort_pending_stops_on_usage_limit(tmp_path):
    a = Archive(tmp_path / "archive")
    a.add([rec(1, "x"), rec(2, "y")])
    state = {"groups": {}, "sorted_ids": []}

    def runner(prompt, schema):
        raise UsageLimit("usage limit reached")

    with pytest.raises(UsageLimit):
        sort_pending(a, state, runner=runner, batch_size=1, questions_path=tmp_path / "q.jsonl")
    assert state["sorted_ids"] == []



def q(qid, company, title):
    return {"qid": qid, "company": company, "college": "IIT Delhi", "date": "2026-10-01",
            "role": "fte", "title": title, "text": title, "topics": ["Arrays"],
            "source_ids": [int(qid.split("-")[0])], "duplicate_of": None}


def test_dedupe_marks_repeats_per_company():
    old = [q("1-1", "Amazon", "Two sum"), q("2-1", "Google", "LRU cache")]
    new = [q("9-1", "Amazon", "Two Sum (pairs)"), q("9-2", "Amazon", "Max flow"),
           q("10-1", "Visa", "Only one")]
    prompts = []

    def runner(prompt, schema):
        prompts.append(prompt)
        return {"matches": [{"qid": "9-1", "duplicate_of": "1-1"},
                            {"qid": "9-2", "duplicate_of": None}]}

    assert dedupe(new, old + new, runner=runner) == {"9-1": "1-1"}
    assert len(prompts) == 1  # Visa has nothing to compare with -> no call
    assert "LRU cache" not in prompts[0]  # only the same company is shown


def test_dedupe_ignores_invalid_targets():
    old = [q("1-1", "Amazon", "Two sum")]
    new = [q("9-1", "Amazon", "x")]
    runner = lambda p, s: {"matches": [{"qid": "9-1", "duplicate_of": "404-1"}]}
    assert dedupe(new, old + new, runner=runner) == {}


def test_apply_duplicates(tmp_path):
    p = tmp_path / "q.jsonl"
    append_jsonl(p, [q("1-1", "Amazon", "a"), q("9-1", "Amazon", "a again")])
    apply_duplicates(p, {"9-1": "1-1"})
    assert [r["duplicate_of"] for r in read_jsonl(p)] == [None, "1-1"]



def test_to_questions_canonicalises_names():
    rows = to_questions([share(company="Zomato", college="IIT (ISM) Dhanbad")], {6827})
    assert rows[0]["company"] == "Eternal (Zomato)" and rows[0]["college"] == "IIT Dhanbad"


def test_normalize_rows():
    rows = normalize_rows([dict(q("1-1", "Eternal", "a"), college="NIT Karnataka")])
    assert rows[0]["company"] == "Eternal (Zomato)" and rows[0]["college"] == "NIT Surathkal"


def test_dedupe_all_only_points_backwards():
    rows = [q("1-1", "Harness", "Max memory"), q("2-1", "Harness", "Max memory again"),
            q("3-1", "Harness", "Max memory 3")]
    # Claude marks a cycle and a forward pointer; only backward pointers are kept.
    runner = lambda p, s: {"matches": [{"qid": "1-1", "duplicate_of": "2-1"},
                                       {"qid": "2-1", "duplicate_of": "1-1"},
                                       {"qid": "3-1", "duplicate_of": "2-1"}]}
    assert dedupe(rows, rows, runner=runner) == {"2-1": "1-1", "3-1": "2-1"}


def test_apply_duplicates_resolves_chains(tmp_path):
    p = tmp_path / "q.jsonl"
    append_jsonl(p, [q("1-1", "Harness", "a"), q("2-1", "Harness", "a"), q("3-1", "Harness", "a")])
    apply_duplicates(p, {"2-1": "1-1", "3-1": "2-1"})
    assert [r["duplicate_of"] for r in read_jsonl(p)] == [None, "1-1", "1-1"]


def test_to_questions_keeps_only_real_leetcode_matches():
    from oa.leetcode import Problems
    probs = Problems([{"id": 1, "title": "Two Sum", "slug": "two-sum", "difficulty": "Easy"}])
    qs = [{"title": "A", "text": "a", "topics": ["Arrays"], "leetcode": {"number": 1, "title": "Two sum"}},
          {"title": "B", "text": "b", "topics": ["Arrays"], "leetcode": {"number": 1, "title": "Made up"}},
          {"title": "C", "text": "c", "topics": ["Arrays"], "leetcode": None}]
    rows = to_questions([share(questions=qs)], {6827}, probs)
    assert rows[0]["leetcode"]["slug"] == "two-sum"
    assert rows[1]["leetcode"] is None and rows[2]["leetcode"] is None
    assert all(r["rev"] == 2 and r["md"] for r in rows)


def test_enrich_retags_resumably(tmp_path):
    from oa.sort import enrich, write_rows
    path = tmp_path / "q.jsonl"
    base = {"company": "TI", "college": "IIT BHU", "date": "2026-10-25", "role": "fte",
            "text": "t", "source_ids": [1], "duplicate_of": None}
    write_rows(path, [dict(base, qid="1-1", title="Op-amp", topics=["Other"]),
                      dict(base, qid="1-2", title="NMOS", topics=["Other"]),
                      dict(base, qid="1-3", title="Repost", topics=["Other"], duplicate_of="1-1"),
                      dict(base, qid="1-4", title="Done", topics=["Arrays"], rev=2)])
    seen = []

    def runner(prompt, schema):
        seen.append(prompt)
        if len(seen) == 1:
            return {"items": [{"qid": "1-1", "topics": ["Analog Electronics"], "leetcode": None},
                              {"qid": "9-9", "topics": ["DP"], "leetcode": None}]}  # not asked: ignored
        raise UsageLimit("You've hit your session limit")

    with pytest.raises(UsageLimit):
        enrich(path, runner=runner, batch_size=1)
    rows = {r["qid"]: r for r in read_jsonl(path)}
    assert rows["1-1"]["topics"] == ["Analog Electronics"] and rows["1-1"]["rev"] == 2
    assert rows["1-2"]["topics"] == ["Other"] and "rev" not in rows["1-2"]  # resumes here
    assert "[1-1] TI: Op-amp" in seen[0] and "Repost" not in "".join(seen) and "Done" not in "".join(seen)


def test_group_context_and_rank():
    from oa.sort import group_context, group_rank
    groups = {"accenture-oa": {"name": "Accenture OA", "company": "Accenture", "role": "OA preparation"},
              "campus-iit-kharagpur-placements": {"name": "IIT Kharagpur Placement Discussion",
                                                  "company": "IIT Kharagpur", "role": "Campus"},
              "campus-iit-delhi-placements": {"name": "IIT Delhi Placement Discussion",
                                              "company": "IIT Delhi", "role": "Campus"},
              "inter-iit": {"name": "Placement '26 OA", "company": "Placement 2026", "role": None}}
    assert "the company is Accenture" in group_context("accenture-oa", groups)
    assert "held at IIT Delhi" in group_context("campus-iit-delhi-placements", groups)
    assert "OAHelper placement group" in group_context("unknown-slug", groups)
    order = sorted(groups, key=lambda s: group_rank(s, groups))
    assert order == ["accenture-oa", "campus-iit-kharagpur-placements", "inter-iit", "campus-iit-delhi-placements"]


def _two_group_archive(tmp_path, monkeypatch):
    import oa.sort as sort_mod
    monkeypatch.setattr(sort_mod, "load_groups", lambda: {
        "acc": {"name": "Accenture OA", "company": "Accenture", "role": "OA preparation"},
        "inter-iit": {"name": "Placement '26 OA", "company": "Placement 2026", "role": None}})
    archive = Archive(tmp_path / "archive")
    archive.add([dict(rec(i, f"msg {i}"), group="inter-iit" if i % 2 else "acc") for i in range(1, 7)])
    return archive


def test_sort_pending_fills_batches_across_groups(tmp_path, monkeypatch):
    archive = _two_group_archive(tmp_path, monkeypatch)
    prompts = []

    def runner(prompt, schema):
        prompts.append(prompt)
        return {"shares": []}

    state = {"groups": {}, "sorted_ids": []}
    sort_pending(archive, state, runner=runner, batch_size=10, questions_path=tmp_path / "q.jsonl")
    assert len(prompts) == 1
    p = prompts[0]
    acc, inter = p.index("group for Accenture OAs"), p.index("OAHelper group \"Placement '26 OA\"")
    assert p.count("\n── Posted in:") == 2 and acc < inter
    for i in (2, 4, 6):
        assert acc < p.index(f"[{i}] ") < inter
    for i in (1, 3, 5):
        assert p.index(f"[{i}] ") > inter
    assert sorted(state["sorted_ids"]) == [1, 2, 3, 4, 5, 6]


def test_sort_pending_cuts_batches_at_batch_size(tmp_path, monkeypatch):
    archive = _two_group_archive(tmp_path, monkeypatch)
    prompts = []
    sort_pending(archive, {"groups": {}, "sorted_ids": []},
                 runner=lambda prompt, schema: prompts.append(prompt) or {"shares": []},
                 batch_size=4, questions_path=tmp_path / "q.jsonl")
    assert len(prompts) == 2


def test_dedupe_pending_folds_new_reposts_and_marks_checked(tmp_path):
    p = tmp_path / "q.jsonl"
    old = q("1-1", "Amazon", "Two sum")
    new = [dict(q("9-1", "Amazon", "Two Sum again"), deduped=False),
           dict(q("9-2", "Amazon", "Max flow"), deduped=False)]
    append_jsonl(p, [old] + new)
    runner = lambda pr, s: {"matches": [{"qid": "9-1", "duplicate_of": "1-1"}]}
    assert dedupe_pending(p, runner=runner) == 2
    rows = read_jsonl(p)
    assert [r["duplicate_of"] for r in rows] == [None, "1-1", None]
    assert [r.get("deduped") for r in rows] == [None, True, True]


def test_dedupe_pending_saves_progress_on_usage_limit(tmp_path):
    p = tmp_path / "q.jsonl"
    append_jsonl(p, [q("1-1", "Amazon", "Two sum"),
                     dict(q("9-1", "Amazon", "Two sum again"), deduped=False),
                     q("2-1", "Google", "LRU"), dict(q("8-1", "Google", "LRU again"), deduped=False)])

    def runner(prompt, schema):
        if "LRU again" in prompt:
            raise UsageLimit("limit")
        return {"matches": [{"qid": "9-1", "duplicate_of": "1-1"}]}

    with pytest.raises(UsageLimit):
        dedupe_pending(p, runner=runner)
    rows = {r["qid"]: r for r in read_jsonl(p)}
    assert rows["9-1"]["duplicate_of"] == "1-1" and rows["9-1"]["deduped"] is True
    assert rows["8-1"]["deduped"] is False


def test_dedupe_pending_ignores_rows_without_flag(tmp_path):
    p = tmp_path / "q.jsonl"
    append_jsonl(p, [q("1-1", "Amazon", "a"), q("2-1", "Amazon", "b")])
    calls = []
    assert dedupe_pending(p, runner=lambda pr, s: calls.append(pr)) == 0
    assert calls == [] and all("deduped" not in r for r in read_jsonl(p))


def test_run_claude_reads_usage_and_keeps_a_reserve(monkeypatch):
    import json as _json
    import subprocess as _sp
    import oa.sort as sort_mod

    def fake_run(cmd, **kw):
        assert "--model" in cmd and "stream-json" in cmd
        events = [{"type": "system", "subtype": "init"},
                  {"type": "rate_limit_event", "rate_limit_info": {"unifiedWindows": {
                      "five_hour": {"utilization": 0.93}}}},
                  {"type": "result", "subtype": "success", "is_error": False, "structured_output": {"x": 1}}]
        return _sp.CompletedProcess(cmd, 0, "\n".join(_json.dumps(e) for e in events), "")

    monkeypatch.setattr(sort_mod.subprocess, "run", fake_run)
    monkeypatch.setitem(sort_mod.USAGE, "five_hour", None)
    assert sort_mod.run_claude("p", {}, model="haiku") == {"x": 1}  # usage unknown: runs
    assert sort_mod.USAGE["five_hour"] == 0.93
    with pytest.raises(UsageLimit, match="10% of the 5-hour limit free"):
        sort_mod.run_claude("p", {}, model="haiku")  # 93% used: no new call
