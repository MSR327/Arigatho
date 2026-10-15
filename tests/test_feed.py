from oa.feed import author_tag, parse_message

RAW = {
    "id": 6827, "client_message_id": "x", "body": "", "author_name": "Ray0ft6_IITD",
    "avatar_slug": "p", "user_id": 20490, "is_mine": False,
    "created_at": "2026-10-14T21:52:01.17629+00:00", "edited_at": None, "deleted": False,
    "attachment": {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1772999,
                   "is_image": False, "inline": True},
    "mentioned_user_ids": [],
    "reply_to": {"id": 6808, "user_id": 16152, "author_name": "Leo0cgo_NITR",
                 "body": "I want rystad Energy oa questions ? Pls dm me or send"},
    "help_reward": None, "help_status": None,
}


def test_author_tag():
    assert author_tag("Ray0ft6_IITD") == "IITD"
    assert author_tag("abc_iitkgp") == "IITKGP"
    assert author_tag("NoTagHere") is None
    assert author_tag(None) is None


def test_parse_message_keeps_content_drops_identity():
    rec = parse_message(RAW, "inter-iit")
    assert rec == {
        "id": 6827, "group": "inter-iit", "sent_at": "2026-10-14T21:52:01.17629+00:00",
        "text": "", "author_tag": "IITD",
        "reply_to": {"id": 6808, "text": "I want rystad Energy oa questions ? Pls dm me or send",
                     "author_tag": "NITR"},
        "attachment": {"name": "rystad (1).pdf", "mime": "application/pdf", "size": 1772999,
                       "is_image": False},
        "deleted": False,
    }
    assert "Ray0ft6" not in str(rec) and "20490" not in str(rec)


def test_parse_message_plain_text():
    raw = dict(RAW, id="7000", body="Amazon OA at KGP: 2 DSA", attachment=None, reply_to=None)
    rec = parse_message(raw, "inter-nit")
    assert rec["id"] == 7000 and rec["text"] == "Amazon OA at KGP: 2 DSA"
    assert rec["attachment"] is None and rec["reply_to"] is None
