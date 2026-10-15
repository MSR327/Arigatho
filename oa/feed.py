"""Turn OAHelper feed messages into archive records (no names, no user ids)."""

import re

TAG_RE = re.compile(r"_([A-Za-z][A-Za-z0-9]{1,11})$")


def author_tag(name):
    m = TAG_RE.search(name or "")
    return m.group(1).upper() if m else None


def parse_message(raw, group):
    att = raw.get("attachment")
    reply = raw.get("reply_to")
    return {
        "id": int(raw["id"]),
        "group": group,
        "sent_at": raw["created_at"],
        "text": raw.get("body") or "",
        "author_tag": author_tag(raw.get("author_name")),
        "reply_to": {
            "id": int(reply["id"]),
            "text": reply.get("body") or "",
            "author_tag": author_tag(reply.get("author_name")),
        } if reply else None,
        "attachment": {
            "name": att.get("name") or "file",
            "mime": att.get("mime") or "",
            "size": int(att.get("size") or 0),
            "is_image": bool(att.get("is_image")),
        } if att else None,
        "deleted": bool(raw.get("deleted")),
    }
