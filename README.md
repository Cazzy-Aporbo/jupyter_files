# Jupyter Files Repository

This repository is a curated collection of Jupyter Notebooks that progress from **Python fundamentals** to **domain-specific health data extraction** and **advanced visualizations**, and now extends into **LLM applications for women’s health**.

It is written from the perspective of an experienced researcher and data scientist: step-by-step, reproducible, and mindful of ethics and compliance.

---

## Repository Structure

| Folder / File                                                                                      | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`basics/`](./basics/)                                                                             | Introductory notebooks covering Python fundamentals.                                                                                               |
| [`basics/python_basics_demo.ipynb`](./basics/python_basics_demo.ipynb)                             | Walkthrough of arithmetic, strings, collections, control flow, functions, classes, NumPy, and Pandas.                                              |
| [`health-data/`](./health-data/)                                                                   | Domain-focused notebooks for health and biomedical workflows.                                                                                      |
| [`health-data/pubmed_extraction_improved.ipynb`](./health-data/pubmed_extraction_improved.ipynb)   | PubMed extraction in synthetic (offline) and Entrez (online) modes with JSON packaging for LLMs.                                                   |
| [`health-data/README_pubmed_extraction.md`](./health-data/README_pubmed_extraction.md)             | Usage guide for the PubMed extraction notebook.                                                                                                    |
| [`models/`](./models/)                                                                             | LLM-focused notebooks.                                                                                                                             |
| [`models/Womens_Health_LLM_Model_improved.ipynb`](./models/Womens_Health_LLM_Model_improved.ipynb) | Demonstrates the use of large language models for women’s health tasks, with reproducibility and ethics checks.                                    |
| [`visuals/`](./visuals/)                                                                           | Visualization notebooks using Matplotlib.                                                                                                          |
| [`visuals/advanced_visuals.ipynb`](./visuals/advanced_visuals.ipynb)                               | Advanced visualizations with a sage/green ombre theme (time-series CI bands, heatmaps, ridge plots, hexbins, stacked areas, parallel coordinates). |
| [`LICENSE`](./LICENSE)                                                                             | Project license (MIT or CC BY recommended).                                                                                                        |
| [`README.md`](./README.md)                                                                         | This file. Repository overview and documentation.                                                                                                  |

---

## Notebook Progression

| Level                | Notebooks                                                                                          | Skills Demonstrated                                                                                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Foundations**      | [`basics/python_basics_demo.ipynb`](./basics/python_basics_demo.ipynb)                             | Variables, types, control flow, collections, functions, classes, file I/O, NumPy, Pandas                                                    |
| **Extraction**       | [`health-data/pubmed_extraction_improved.ipynb`](./health-data/pubmed_extraction_improved.ipynb)   | PubMed API access (Entrez), synthetic data simulation, caching, JSON packaging for LLMs                                                     |
| **Visualization**    | [`visuals/advanced_visuals.ipynb`](./visuals/advanced_visuals.ipynb)                               | Matplotlib-only visuals with custom sage/green ombre theme: CI bands, heatmaps, violin and ridge plots, stacked areas, parallel coordinates |
| **LLM Applications** | [`models/Womens_Health_LLM_Model_improved.ipynb`](./models/Womens_Health_LLM_Model_improved.ipynb) | Using large language models for women’s health data, including preprocessing, inference, and ethics safeguards                              |

---

## Typical Workflow

```
[ Python Basics ] → [ Data Extraction ] → [ Data Cleaning ] → [ Visualization ] → [ LLM Applications ]
```

* Reinforce fundamentals with the basics notebook
* Explore biomedical workflows with the PubMed extraction notebook
* Present findings with advanced, publication-quality visuals
* Experiment with domain-specific LLM applications in women’s health

---

## Example Visuals

| Visualization Type        | Use Case                              |
| ------------------------- | ------------------------------------- |
| Time-series with CI bands | Tracking changes with uncertainty     |
| Heatmaps                  | Correlation structures                |
| Violin / Ridge plots      | Distribution and subgroup comparisons |
| Hexbin scatter            | Dense relationships                   |
| Stacked areas             | Compositional time trends             |
| Parallel coordinates      | Multivariate comparisons              |

---

## Installation & Setup

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pandas numpy requests biopython faker matplotlib torch transformers jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

---

## Ethics & Compliance

* **No PHI/PII**: All datasets must be de-identified before use.
* **NCBI Entrez**: When using PubMed, set a valid email in `Bio.Entrez` and respect rate limits.
* **Bias Awareness**: Women’s health data is often underrepresented; model evaluation must account for subgroup fairness.
* **Transparency**: Document limitations and assumptions in any analysis.

---

## Roadmap

| Version | Planned Additions                                              |
| ------- | -------------------------------------------------------------- |
| v0.1    | Python basics demo + initial PubMed extraction                 |
| v0.2    | Improved PubMed extraction with caching and JSON export        |
| v0.3    | Advanced visualization notebooks (sage/green ombre theme)      |
| v0.4    | Women’s Health LLM notebook with preprocessing and ethics      |
| v0.5    | Interactive visuals (Plotly, Altair) and dashboard outputs     |
| v0.6    | Bias detection and explainability extensions for LLM notebooks |

---

