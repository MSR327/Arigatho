import json

from oa.store import Archive, attachment_relpath, load_state, save_state


def rec(i, month="2026-10", group="inter-iit", att=None):
    return {"id": i, "group": group, "sent_at": f"{month}-05T10:00:00+00:00", "text": f"m{i}",
            "author_tag": None, "reply_to": None, "attachment": att, "deleted": False}


def test_add_dedupes_and_splits_by_month(tmp_path):
    a = Archive(tmp_path)
    assert [r["id"] for r in a.add([rec(1, "2026-09"), rec(2)])] == [1, 2]
    assert [r["id"] for r in a.add([rec(2), rec(3)])] == [3]
    assert (tmp_path / "inter-iit" / "2026-09.jsonl").exists()
    assert len((tmp_path / "inter-iit" / "2026-10.jsonl").read_text().splitlines()) == 2
    assert [r["id"] for r in Archive(tmp_path).all()] == [1, 2, 3]
    assert set(Archive(tmp_path).by_id()) == {1, 2, 3}


def test_attachment_relpath():
    att = {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1, "is_image": False}
    assert attachment_relpath(rec(6827, att=att)) == "archive/files/6827-rystad_1_.pdf"
    assert attachment_relpath(rec(5)) is None


def test_state_roundtrip(tmp_path):
    p = tmp_path / "state.json"
    assert load_state(p) == {"groups": {}, "sorted_ids": []}
    save_state(p, {"groups": {"inter-iit": {"oldest_id": 1}}, "sorted_ids": [1]})
    assert json.loads(p.read_text())["sorted_ids"] == [1]
    assert load_state(p)["groups"]["inter-iit"]["oldest_id"] == 1
