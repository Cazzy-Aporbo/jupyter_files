# Jupyter Files Repository

This repository is a work in progress. It will be a curated collection of Jupyter Notebooks that progress from **Python fundamentals** to **domain-specific data extraction** and **advanced data visualization**. It is designed as a structured resource for learning, experimenting, and building reproducible workflows.

---

## Repository Structure

| Folder / File                                  | Description                                                                                                     |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `basics/`                                      | Introductory notebooks demonstrating Python fundamentals.                                                       |
| `basics/python_basics_demo.ipynb`              | Covers arithmetic, strings, collections, control flow, functions, classes, NumPy, Pandas.                       |
| `health-data/`                                 | Domain-focused notebooks for working with health and biomedical data.                                           |
| `health-data/pubmed_extraction_improved.ipynb` | Notebook demonstrating PubMed extraction in synthetic (offline) and Entrez (online) modes, with JSON packaging. |
| `README_pubmed_extraction.md`                  | Detailed usage guide for the PubMed extraction notebook.                                                        |
| `LICENSE`                                      | Project license (MIT or CC BY recommended).                                                                     |
| `README.md`                                    | This file. Overview of the entire repository.                                                                   |

---

## Notebook Progression

| Level                                   | Notebooks                                      | Skills Demonstrated                                                                      |
| --------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Foundations**                         | `basics/python_basics_demo.ipynb`              | Variables, types, control flow, collections, functions, classes, file I/O, NumPy, Pandas |
| **Extraction**                          | `health-data/pubmed_extraction_improved.ipynb` | PubMed API access, synthetic data simulation, caching, JSON packaging for LLMs           |
| **Visualization** (planned/coming soon) | `visuals/` (future folder)                     | Matplotlib, Seaborn, Pandas visualization, interactive charts                            |

---

## Typical Workflow

```text
[ Python Basics ] → [ Data Extraction ] → [ Data Cleaning ] → [ Visualization ]
```

* Start with the basics notebook to reinforce core skills.
* Move into extraction notebooks to practice working with **real or simulated data sources**.
* Apply cleaning, transformation, and exploratory analysis.
* Generate **advanced visuals** to interpret and present findings.

---

## Example Visuals

This repository includes or will include advanced visualization notebooks. Typical outputs:

| Visualization Type | Use Case                                |
| ------------------ | --------------------------------------- |
| Line / Bar charts  | Trends over time, category comparisons  |
| Scatter plots      | Relationships between numeric variables |
| Heatmaps           | Correlations and matrix-style data      |
| Box/Violin plots   | Distribution and variance insights      |

---

## Installation & Setup

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -U pandas numpy requests biopython faker matplotlib seaborn jupyter
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
| v0.3    | Advanced visualization notebooks with Seaborn and Pandas         |
| v0.4    | Interactive visuals (Plotly, Altair) and dashboard-ready outputs |

---

Do you want me to also generate a **table of contents with direct links to each notebook** (so GitHub renders them as clickable)?
