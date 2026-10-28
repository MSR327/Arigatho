import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture(autouse=True)
def private_logs(tmp_path, monkeypatch):
    """Tests log to a temp folder, never to the tracker's real logs/run.log."""
    import oa.common
    import oa.sort
    monkeypatch.setattr(oa.common, "LOGS", tmp_path / "logs")
    monkeypatch.setattr(oa.sort, "LOGS", tmp_path / "logs")
