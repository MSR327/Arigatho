import pytest

from oa.sort import (ClaudeError, UsageLimit, build_batch_prompt, format_message, is_sortable,
                     sort_pending, to_questions)
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
