# Capital Bikeshare (April 2025) — SQL + Python Analysis

> **664,199 bike trips. 6 SQL questions. 2 execution environments (SQLite + BigQuery). Fully tested and CI-verified.**

End-to-end data engineering and analytics project: raw trip data → SQL analysis → automated Python visualisations → interactive cloud map, all guarded by a `pytest` suite and a GitHub Actions CI/CD pipeline that runs on every commit.

**Data source:** [Capital Bikeshare system data](https://capitalbikeshare.com/system-data) (April 2025 monthly release)

| Stat | Value |
|------|-------|
| Rows analysed | ~664,199 trips |
| SQL queries | 6 (SQLite) + 1 (BigQuery) |
| Test files | 7 (`pytest`) |
| Linters / formatters | `black`, `flake8`, `ruff` |
| CI | GitHub Actions (lint + test on every push) |
| Execution environments | SQLite (local) · BigQuery (cloud) |

---

## Overview
This project analyzes **Capital Bikeshare trip data for April 2025** to understand usage patterns across stations, routes, time of day, trip duration, weekday, and rider type.

The repo supports two complementary workflows:
- **SQLite (local, reproducible)**: run SQL locally and generate static plots/maps  
  (`sql_scripts/` + `python_scripts/`)
- **BigQuery (cloud, scalable + interactive outputs)**: query in BigQuery, export CSV, and generate interactive outputs  
  (`bigquery_queries/`)

---

## Questions Answered
- Which stations and routes are most used?
- What time of day are rides most frequent?
- How long are the trips?
- How does usage vary by weekday?
- Who uses the system more: casual riders or members?

➡️ **See [ANALYSIS.md](ANALYSIS.md) for the full SQL walkthroughs, query explanations, and result tables.**

---

## Repository Layout
- `sql_scripts/` — SQL queries against the `trips` table (SQLite workflow)
- `python_scripts/` — SQLite query runners + plotting/map utilities (outputs saved to `figures/`)
- `bigquery_queries/` - BigQuery workflow scripts/notebook + interactive plotting/app
- `figures/` - generated static charts/maps
- `tests/` - tests that validate key outputs are produced
- `.github/workflows/ci.yml` - CI pipeline for linting + tests

---

## CI/CD & Testing

**This is the part of the project I'm most proud of.** Every commit triggers a GitHub Actions workflow that:

1. Runs `ruff`, `black --check`, and `flake8` to enforce code style
2. Executes the full `pytest` suite to verify that all figure/artifact outputs are actually produced

The test suite (`tests/`) covers:
- Plot generation (hourly trips, duration distribution, weekday breakdown)
- Map output (static PNG map of top stations)
- BigQuery plotting module import and CSV-driven artifact creation
- Trip bin categorisation logic
- Dummy smoke tests to guard against import errors

This means the project can be cloned, the environment set up, and the entire pipeline re-run with confidence that nothing is silently broken. CI also serves as living documentation: the workflow file shows exactly which quality gates must pass before a change is accepted.

---

## Setup (Python)
Create/activate a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Quality checks + tests
```bash
ruff check . --fix
black .
flake8 .
pytest tests/
```

---

## Workflow A: SQLite (Local Analysis)
The SQLite workflow is designed for portable, offline analysis using a local database.

- SQL query files live in `sql_scripts/` and assume a `trips` table.
- Plot/map generation utilities are in `python_scripts/`.
- Outputs are saved to `figures/`.

Typical flow:
1. Load/build the SQLite database containing the `trips` table (see repo scripts/config for the expected DB path).
2. Run SQL scripts in `sql_scripts/` against that database.
3. Use `python_scripts/` to generate plots and maps from query outputs.

---

## Workflow B: BigQuery (Cloud Analysis + Heatmap)
The BigQuery workflow supports scalable querying, then exports results (optionally to CSV) to power plotting and an interactive map.

Set environment variables and run the BigQuery scripts:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/tmp/gcp_key.json
export BQ_PROJECT_ID=capitalbikeshare-489408
export BQ_TABLE_ID=capitalbikeshare-489408.02_2026.tripdata
# optional: export BQ_OUTPUT_CSV=tripdata.csv

python bigquery_queries/scripts.py
python bigquery_queries/plotting.py
```

This produces:
- `tripdata.csv` (optional query output, depending on configuration)
- `heatmap.html` (interactive Plotly map)

### Optional Interactive App
```bash
streamlit run bigquery_queries/app.py
```

---
### BigQuery heatmap showcase
![BigQuery Heatmap Screenshot](screenshot_heatmap.png)

The interactive heatmap generated from the BigQuery workflow is saved as `heatmap.html`.  
If you want a quick browser preview without cloning, you can use an HTML preview service (as long as `heatmap.html` is accessible from the repo).

---

## SQL & Engineering Skills Demonstrated

| Skill | Where used | Why this choice |
|-------|-----------|-----------------|
| `WHERE` / `IS NOT NULL` guards | All queries | 180k NULL station rows would skew aggregations; explicit guards make the filter intent visible |
| `GROUP BY` + `COUNT` / `AVG` | Station, hour, weekday, rider-type queries | Standard aggregation pattern; keeps queries readable |
| `strftime()` / `julianday()` | Hour-of-day and duration queries | SQLite-native time functions avoid importing a datetime library |
| `CASE WHEN` binning | Duration distribution | Inline binning avoids a second query pass or post-processing in Python |
| CTEs (`WITH` clauses) | Duration and weekday queries | Separates data-prep from aggregation; easier to read, test, and extend than nested subqueries |
| Window functions (`SUM(...) OVER ()`) | Rider-type share query | Computes group percentages in a single table scan, removing a correlated subquery |
| Python + SQLite / BigQuery | `python_scripts/`, `bigquery_queries/` | Keeps query logic in `.sql` files and rendering logic in Python — each layer is independently testable |
| `pytest` test suite | `tests/` | Catches silent regressions (e.g. a plot that runs but writes an empty file) |
| `black` / `flake8` / `ruff` | Entire repo | Consistent formatting removes style noise from code reviews |
| GitHub Actions CI | `.github/workflows/ci.yml` | Lint + test gates run on every push, making the pipeline reproducible by anyone who clones the repo |

---

## Architecture / Design Decisions

### May 2025: Reproducibility + CI Foundations
- Central `config.py` for global paths (`FIGURES_DIR`, database location) — one change propagates everywhere
- Automated plot generation for all major SQL outputs
- `pytest`-based test suite to ensure figures are created and contain data
- CI/CD with GitHub Actions to automate lint checks and test execution on every commit
- Code formatting (`black`) and linting (`flake8`, `ruff`) configured and enforced in CI
- Logical file structure: `python_scripts/` for rendering, `tests/` for validation, `figures/` for outputs

### March 2026: BigQuery Integration & Enhanced Workflows

#### BigQuery Integration
- **Cloud-ready query workflow**: BigQuery query execution in `bigquery_queries/scripts.py` and `bigquery_queries/eda.ipynb`
- **Python query execution**: `scripts.py` reads `BQ_PROJECT_ID`, `BQ_TABLE_ID`, and optional `BQ_OUTPUT_CSV`, runs a grouped BigQuery query, and saves results for downstream plotting
- **Interactive exploration**: Jupyter notebook demonstrates query execution, result processing, and visualisation interactively
- **Visualisation pipeline**: `plotting.py` and `app.py` transform BigQuery CSV outputs into interactive HTML maps/charts using Plotly and Folium

#### CSV-Based Workflow
- **Decoupled data and visualisation**: BigQuery results written to CSV so plotting runs offline
- **Portable outputs**: CSV artifacts can be version-controlled, shared, and reused without re-running expensive queries
- **Local and cloud flexibility**: plots generated from either SQLite (local) or BigQuery (cloud) data sources

#### Enhanced Modularity
- **Separation of concerns**: query logic, data processing, and visualisation isolated in dedicated modules
- **Reusable components**: functions in `scripts.py` and `plotting.py` support multiple query types and output formats
- **Configuration management**: centralised `config.py` ensures consistent paths across local and CI environments

#### Robust Testing & CI
- **Expanded test coverage**: tests validate plotting functions, HTML/PNG artifact creation, and BigQuery plotting module imports
- **Import path resolution**: `conftest.py` ensures `config.py` and project modules are discoverable in all environments (local, Docker, GitHub Actions)
- **Automated quality checks**: GitHub Actions runs `pytest`, `black`, `flake8`, and `ruff` on every commit

---

## Key Findings

- Most trips are short: average duration **16.1 minutes**, most trips **5–15 minutes**
- Most popular starting station: **Columbus Circle / Union Station** (5,462 trips)
- **Tuesdays and Wednesdays** are the busiest days; **Mondays and Fridays** are quietest
- **~70%** of trips are taken by members
- Trip volume peaks at commuting windows: **7–9 AM** and **4–6 PM**

➡️ **Full query walkthroughs, result tables, and charts: [ANALYSIS.md](ANALYSIS.md)**
