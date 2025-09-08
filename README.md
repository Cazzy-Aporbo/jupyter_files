
# Jupyter Files Repository

This repository is a work in progress. It will be a curated collection of Jupyter Notebooks that progress from **Python fundamentals** to **domain-specific data extraction** and **advanced data visualization**. It is designed as a structured resource for learning, experimenting, and building reproducible workflows.

* [Repository Structure](#repository-structure)
* [Notebook Progression](#notebook-progression)
* [Typical Workflow](#typical-workflow)
* [Example Visuals](#example-visuals)
* [Installation & Setup](#installation--setup)
* [Ethics & Compliance](#ethics--compliance)
* [Roadmap](#roadmap)
* [Documentation Links](#documentation-links)

---

## Repository Structure

| Folder / File                                                                                    | Description                                                                               |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [`basics/`](./basics/)                                                                           | Introductory notebooks demonstrating Python fundamentals.                                 |
| [`basics/python_basics_demo.ipynb`](./basics/python_basics_demo.ipynb)                           | Covers arithmetic, strings, collections, control flow, functions, classes, NumPy, Pandas. |
| [`health-data/`](./health-data/)                                                                 | Domain-focused notebooks for working with health and biomedical data.                     |
| [`health-data/pubmed_extraction_improved.ipynb`](./health-data/pubmed_extraction_improved.ipynb) | PubMed extraction in synthetic (offline) and Entrez (online) modes, with JSON packaging.  |
| [`health-data/README_pubmed_extraction.md`](./health-data/README_pubmed_extraction.md)           | Usage guide for the PubMed extraction notebook.                                           |
| [`visuals/`](./visuals/)                                                                         | Advanced visualization notebooks.                                                         |
| [`visuals/advanced_visuals.ipynb`](./visuals/advanced_visuals.ipynb)                             | Matplotlib-only advanced visuals (sage/green ombre theme).                                |
| [`LICENSE`](./LICENSE)                                                                           | Project license (MIT or CC BY recommended).                                               |
| [`README.md`](./README.md)                                                                       | Overview of the repository (this file).                                                   |

---

## Notebook Progression

| Level             | Notebooks                                                                                        | Skills Demonstrated                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Foundations**   | [`basics/python_basics_demo.ipynb`](./basics/python_basics_demo.ipynb)                           | Variables, types, control flow, collections, functions, classes, file I/O, NumPy, Pandas            |
| **Extraction**    | [`health-data/pubmed_extraction_improved.ipynb`](./health-data/pubmed_extraction_improved.ipynb) | PubMed API access (Entrez), synthetic data simulation, caching, JSON packaging for LLMs             |
| **Visualization** | [`visuals/advanced_visuals.ipynb`](./visuals/advanced_visuals.ipynb)                             | Matplotlib, correlation heatmaps, CI bands, ridge plots, hexbins, area charts, parallel coordinates |

---

## Typical Workflow

```
[ Python Basics ] → [ Data Extraction ] → [ Data Cleaning ] → [ Visualization ]
```

* Start with the basics notebook to reinforce core skills.
* Move into extraction notebooks to practice working with real or simulated data sources.
* Apply cleaning, transformation, and exploratory analysis.
* Generate advanced visuals to interpret and present findings.

---

## Example Visuals

This repository includes (or will include) advanced visualization notebooks. Typical outputs:

| Visualization Type   | Use Case                                |
| -------------------- | --------------------------------------- |
| Line / Bar charts    | Trends over time, category comparisons  |
| Scatter plots        | Relationships between numeric variables |
| Heatmaps             | Correlations and matrix-style data      |
| Box/Violin plots     | Distribution and variance insights      |
| Ridge (joy) plots    | Layered group distributions             |
| Hexbin density       | Dense scatter relationships             |
| Parallel coordinates | Multivariate pattern comparison         |

---

## Installation & Setup

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -U pandas numpy requests biopython faker matplotlib jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```


---

## Ethics & Compliance

* **No PHI/PII**: Do not include personally identifiable or health-identifying data in notebooks.
* **NCBI Entrez**: When using PubMed extraction, set a valid email in `Bio.Entrez` and respect usage limits.
* **Attribution**: When publishing results, cite data sources properly (PMIDs, DOIs, etc.).

---

## Roadmap

| Version | Planned Additions                                                |
| ------- | ---------------------------------------------------------------- |
| v0.1    | Python basics demo + initial PubMed extraction notebook          |
| v0.2    | Improved PubMed extraction with caching and JSON export          |
| v0.3    | Advanced visualization notebooks with Matplotlib theme parity    |
| v0.4    | Interactive visuals (Plotly, Altair) and dashboard-ready outputs |

---

## Documentation Links

* Python: [https://docs.python.org/3/](https://docs.python.org/3/)
* Virtual environments: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
* Jupyter Notebook: [https://jupyter-notebook.readthedocs.io/](https://jupyter-notebook.readthedocs.io/)
* NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)
* Pandas: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
* Matplotlib: [https://matplotlib.org/stable/users/index.html](https://matplotlib.org/stable/users/index.html)
* Biopython (Entrez): [https://biopython.org/wiki/Entrez](https://biopython.org/wiki/Entrez)
* NCBI E-utilities (PubMed): [https://www.ncbi.nlm.nih.gov/books/NBK25501/](https://www.ncbi.nlm.nih.gov/books/NBK25501/)

---
