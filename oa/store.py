"""Append-only message archive and the small state file."""

import json
import re

from oa.common import append_jsonl, read_jsonl


class Archive:
    def __init__(self, root):
        self.root = root
        self._ids = None

    def _files(self):
        return sorted(self.root.glob("*/*.jsonl"))

    def all(self):
        rows = [r for f in self._files() for r in read_jsonl(f)]
        return sorted(rows, key=lambda r: r["id"])

    def by_id(self):
        return {r["id"]: r for r in self.all()}

    def add(self, records):
        if self._ids is None:
            self._ids = {r["id"] for r in self.all()}
        new = []
        for r in records:
            if r["id"] in self._ids:
                continue
            self._ids.add(r["id"])
            append_jsonl(self.root / r["group"] / f"{r['sent_at'][:7]}.jsonl", [r])
            new.append(r)
        return new


def attachment_relpath(rec):
    att = rec.get("attachment")
    if not att:
        return None
    safe = re.sub(r"[^A-Za-z0-9.-]+", "_", att["name"])[-80:]
    return f"archive/files/{rec['id']}-{safe}"


def load_state(path):
    if not path.exists():
        return {"groups": {}, "sorted_ids": []}
    return json.loads(path.read_text())


def save_state(path, state):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(path)
