#!/usr/bin/env python3
"""
make_reusable_notebook.py
Creates a fully documented, professional Jupyter Notebook template that teaches
reusability and best practices, plus a small local utils module.

Outputs:
- Reusable_Notebook_Template.ipynb
- notebook_utils.py

Usage:
    python make_reusable_notebook.py

Dependencies:
    pip install nbformat
"""
from __future__ import annotations

import sys
from datetime import datetime
from textwrap import dedent

try:
    import nbformat as nbf
except Exception:
    sys.stderr.write(
        "This script requires 'nbformat'. Install with:\n"
        "    pip install nbformat\n"
    )
    raise

NOTEBOOK_PATH = "Reusable_Notebook_Template.ipynb"
UTILS_MODULE = "notebook_utils.py"


def build_notebook() -> "nbf.NotebookNode":
    nb = nbf.v4.new_notebook()
    cells = []

    author = "Author: Cazandra Aporbo"
    date_str = datetime.now().strftime("%Y-%m-%d")

    # --- Cover ---
    cover_md = f"""# Reusable Jupyter Notebook Template
**{author}**  
**Date:** {date_str}

This notebook is a teaching template designed to help you write **reusable**, **readable**, and **professional** notebooks.
"""

    # --- Example cells (abbreviated for clarity) ---
    howto_md = dedent("""
    ## How to Use This Template
    - Duplicate and rename this file per project.
    - Fill project metadata.
    - Use the `notebook_utils.py` module for reusable functions.
    - Add lightweight tests (assertions).
    - Keep code modular, styled, and well-documented.
    """)

    metadata_code = dedent("""
    from dataclasses import dataclass, field
    from typing import List, Optional
    from pathlib import Path

    @dataclass
    class ProjectMeta:
        project_name: str
        owner: str
        description: str
        data_sources: List[str] = field(default_factory=list)
        outputs: List[str] = field(default_factory=list)
        seed: int = 42
        notebook_path: Optional[str] = None

    META = ProjectMeta(
        project_name="Example Analysis – Reusable Template",
        owner="Cazandra Aporbo",
        description="Demonstrates reusable, modular, and testable patterns.",
        data_sources=[],
        outputs=[],
        seed=42,
        notebook_path=str(Path.cwd())
    )
    META
    """)

    utils_code = dedent('''
    UTILS_PATH = "notebook_utils.py"
    utils_src = """\
from typing import Iterable, List, Any, Callable
from collections import Counter
import math

def find_most_common(values: Iterable[Any]) -> Any:
    counts = Counter(values)
    top_two = counts.most_common(2)
    assert len(top_two) >= 1, "Empty iterable."
    if len(top_two) == 1:
        return top_two[0][0]
    assert top_two[0][1] != top_two[1][1], "There's a tie for most common value."
    return top_two[0][0]

def safe_mean(x: Iterable[float]) -> float:
    x = list(x)
    assert len(x) > 0, "safe_mean() received an empty sequence."
    return sum(x) / len(x)

def zscore(seq: Iterable[float]) -> List[float]:
    data = list(seq)
    mu = safe_mean(data)
    var = sum((v - mu)**2 for v in data) / len(data) if len(data) > 0 else 0.0
    sd = math.sqrt(var) if var > 0 else 1.0
    return [(v - mu)/sd for v in data]
"""
    with open(UTILS_PATH, "w", encoding="utf-8") as f:
        f.write(utils_src)
    print("Wrote utils module ->", UTILS_PATH)
    ''')

    checklist_md = dedent("""
    ## Reusability Checklist
    - [ ] Centralized utilities used
    - [ ] Functions are small, typed, documented
    - [ ] Assertions guard assumptions
    - [ ] Variables are descriptive
    - [ ] Style is consistent (PEP 8)
    """)

    cells.extend([
        nbf.v4.new_markdown_cell(cover_md),
        nbf.v4.new_markdown_cell(howto_md),
        nbf.v4.new_code_cell(metadata_code),
        nbf.v4.new_code_cell(utils_code),
        nbf.v4.new_markdown_cell(checklist_md),
    ])

    nb["cells"] = cells
    return nb


def write_notebook(nb: "nbf.NotebookNode", path: str = NOTEBOOK_PATH) -> None:
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)


def main() -> None:
    nb = build_notebook()
    write_notebook(nb, NOTEBOOK_PATH)
    print(f"Wrote notebook -> {NOTEBOOK_PATH}")
    with open(UTILS_MODULE, "w", encoding="utf-8") as f:
        f.write('"""Boilerplate utils file. Notebook writes richer version."""')
    print(f"Wrote utils module -> {UTILS_MODULE}")


if __name__ == "__main__":
    main()
