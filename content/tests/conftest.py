"""Load each pattern's template.py as a module: `load("sliding-window")`."""
import importlib.util
from pathlib import Path

import pytest

PATTERNS_DIR = Path(__file__).resolve().parent.parent / "patterns"


def _load(slug: str):
    path = PATTERNS_DIR / slug / "template.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def load():
    return _load
