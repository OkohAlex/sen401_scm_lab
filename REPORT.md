# SEN 401 Software Configuration Management and Maintenance
## Individual Laboratory Practical Report

**Student:** Okoh Edache Alex  
**Matric number:** 2023/C/SENG/0389  
**Course:** SEN 401 — Software Configuration Management and Maintenance  
**Submission:** Individual  
**Repository:** [github.com/OkohAlex/sen401_scm_lab](https://github.com/OkohAlex/sen401_scm_lab)  
**Report status:** Draft for evidence insertion; all image boxes below are placeholders.

> **Before submission:** Replace each clearly marked screenshot placeholder with an original screenshot captured from this project and your own GitHub account. Check that the final screenshots show your actual output. This draft intentionally does not contain fabricated screenshots.

## 1. Introduction

This practical demonstrates software configuration management and maintenance through four related laboratory exercises. The work begins with a modular Python student-score application and a version-controlled baseline, then applies corrective, adaptive, perfective, and preventive maintenance. A separate inventory example is used to practice configuration status accounting and change-log generation. The final exercise reverse-engineers the inventory workflow, migrates its sample data into SQLite, exposes it through a FastAPI service, and packages the service with Docker Compose.

All four exercises are organized in separate folders in one individual submission repository. The folder structure keeps each lab's code, dependencies, tests, and instructions together while sharing one Git history for this submission.

## 2. Scope and individual task allocation

This is an individual assessment. The student is responsible for the project setup, code, tests, Git operations, and report preparation across Labs 1–4. The repository and this report identify the work as individual; group-member allocations do not apply.

| Work area | Individual responsibility |
|---|---|
| Lab 1 | Create and run the modular student-score starter; establish the v1.0 baseline. |
| Lab 2 | Maintain and test the student application; tag the v1.1 maintenance release. |
| Lab 3 | Build and test the inventory example; record maintenance changes in the CSA register and changelog. |
| Lab 4 | Analyze module dependencies; implement the FastAPI/SQLite migration and Compose deployment; run tests and endpoint checks. |

## 3. Repository structure

```text
sen401_scm_lab/
|-- README.md
|-- REPORT.md
`-- Labs/
    |-- Lab1/
    |   |-- app.py
    |   |-- students.py
    |   |-- requirements.txt
    |   |-- RELEASE_NOTES.md
    |   `-- utils/helpers.py
    |-- Lab2/
    |   |-- app.py
    |   |-- students.py
    |   |-- requirements.txt
    |   |-- tests/test_helpers.py
    |   `-- utils/helpers.py
    |-- Lab3/
    |   |-- app.py
    |   |-- inventory.py
    |   |-- models.py
    |   |-- tests/test_inventory.py
    |   |-- changelog.txt
    |   `-- status_accounting.csv
    `-- Lab4/
        |-- app/
        |-- data/legacy_inventory.json
        |-- docs/
        |-- tests/test_api.py
        |-- Dockerfile.api
        |-- Dockerfile.db-init
        `-- docker-compose.yml
```

### Screenshot 1 — Repository and lab folder structure

**[SCREENSHOT PLACEHOLDER — Insert an original VS Code Explorer or File Explorer screenshot showing `Labs/Lab1` through `Labs/Lab4` and representative files.]**

## 4. Lab 1 — SCM setup and baseline creation

### Objective

Create a modular Python demonstration with separate sample data, application entry point, and reusable helper functions, then establish a Git baseline.

### Implementation

| File | Purpose |
|---|---|
| `Labs/Lab1/students.py` | Holds sample student names and scores. |
| `Labs/Lab1/utils/helpers.py` | Returns the highest- and lowest-scoring student, safely returning `None` for an empty list. |
| `Labs/Lab1/app.py` | Displays the sample records and score summary. |
| `Labs/Lab1/requirements.txt` | Documents that the starter uses the Python standard library only. |
| `Labs/Lab1/RELEASE_NOTES.md` | Describes the v1.0 starter baseline. |

The application separates data, calculations, and console output. A run from the Lab 1 folder displayed four sample students, identified Zainab as the highest scorer at 91.5, and Kemi as the lowest at 69.5.

### Configuration management

The starter baseline is commit `d26b84e`, tagged `v1.0`. The repository includes `main`, `dev`, `feature/*`, and `maint/*` branches. The `main` branch is configured to require a pull request and one approval before merging; the individual submission changes remain on a feature branch until reviewed.

### Screenshot placeholders

- **[SCREENSHOT PLACEHOLDER — Insert the Lab 1 demo running in a terminal, with the displayed records and highest/lowest results.]**
- **[SCREENSHOT PLACEHOLDER — Insert Git history showing the initial baseline commit and the `v1.0` tag.]**
- **[SCREENSHOT PLACEHOLDER — Insert the repository branch list or GitHub `main` branch protection settings.]**

## 5. Lab 2 — Software maintenance

### Objective

Apply the four maintenance categories to the student-score application and verify the resulting behavior.

### Maintenance changes

| Type | Change |
|---|---|
| Corrective | Handle an empty cohort without attempting an invalid `max`, `min`, or median operation. The score helpers return `None` when there are no students. |
| Adaptive | Use Pydantic models to validate student names and scores; scores must be within 0–100. The code uses Python 3.10+ syntax and was exercised with Python 3.11. |
| Perfective | Add median-score reporting and make the console output clearer. |
| Preventive | Keep the student model/data, score calculations, and console entry point in separate modules; add type hints, docstrings, and regression tests. |

The regression tests cover an empty cohort and a populated cohort. The even-sized test cohort has a median of 75.0. The sample application output reports a median score of 81.0.

### Version control and verification

The maintenance changes were committed as `996df68` on branch `maintenance` and tagged `v1.1`. Two unit tests passed, and the demonstration application ran successfully from `Labs/Lab2`.

### Screenshot placeholders

- **[SCREENSHOT PLACEHOLDER — Insert the Lab 2 unit-test output showing both tests passing.]**
- **[SCREENSHOT PLACEHOLDER — Insert the Lab 2 console output showing highest, lowest, and median scores.]**
- **[SCREENSHOT PLACEHOLDER — Insert Git history showing the maintenance commit, `maintenance` branch, and `v1.1` tag.]**

## 6. Lab 3 — Configuration status accounting and auditing

### Objective

Maintain a small inventory application and record which configuration changes correspond to maintenance activities.

### Implementation and maintenance

The inventory project separates sample records (`inventory.py`), validated immutable records (`models.py`), calculations (`utils/helpers.py`), and console reporting (`app.py`). It calculates total stock value, handles an empty inventory, rejects invalid quantities and prices, and identifies the items with the largest and smallest quantities.

The included sample data produces a total stock value of **$4,328.25**. The wireless keyboard has the largest quantity (25 units); the 27-inch monitor has the smallest quantity (8 units).

Three unit tests cover empty inventory, valuation and quantity extremes, and invalid negative values. All three passed when run from `Labs/Lab3`.

### Status accounting and history

`status_accounting.csv` maps configuration-item identifiers and maintenance categories to commit identifiers, branch names, authors, and dates. `changelog.txt` records the Lab 3 source repository's Git history. Those commit identifiers refer to the Lab 3 project before it was consolidated into this single submission repository; they are retained as provenance and are not represented as commits in the unified repository. The original standalone Lab 3 repository is retained as a backup, not as the requested submission repository.

The Lab 3 source history records baseline `9c70534`, maintenance work `838c460`, and CSA documentation `e1945b6`. Its source release tag `v1.0` points to the completed inventory maintenance commit.

### Screenshot placeholders

- **[SCREENSHOT PLACEHOLDER — Insert Lab 3 test output showing all three tests passing and the inventory demonstration output.]**
- **[SCREENSHOT PLACEHOLDER — Insert `status_accounting.csv` open in an editor, showing the CI-to-change/commit mapping.]**
- **[SCREENSHOT PLACEHOLDER — Insert the Lab 3 Git graph or changelog, clearly identifying it as the source history before consolidation.]**

## 7. Lab 4 — Re-engineering and migration

### Reverse engineering

The earlier student and inventory programs use module-level in-memory lists and console output. Their structure is suitable for small demonstrations, but data is tied to process lifetime and there is no REST interface for another client. The Lab 4 implementation separates API schemas, database connection/schema management, database operations, routes, and seed-data migration.

| Module/service | Responsibility |
|---|---|
| `app/models.py` | Validate request data and define API response schemas. |
| `app/database.py` | Create SQLite connections and initialize the inventory table. |
| `app/controllers.py` | Perform parameterized SQLite reads and inserts. |
| `app/seed.py` | Migrate the JSON inventory into SQLite without duplicating existing items. |
| `app/main.py` | Provide FastAPI health, list, detail, and create endpoints. |
| `db-init` container | Initialize the database and import seed data once. |
| `api` container | Run the HTTP API against the shared persistent database volume. |

**Dependency diagram:** `docs/reverse_engineering.md` includes a Mermaid module/service diagram; `docs/dependency_diagram.mmd` contains its diagram source.

### Migration and API

The source inventory is `data/legacy_inventory.json`. The initializer validates each record and stores it in the SQLite database. The API provides:

| Method and path | Purpose |
|---|---|
| `GET /health` | Return the service health status. |
| `GET /api/v1/inventory` | List inventory records. |
| `GET /api/v1/inventory/{item_id}` | Retrieve one record or return 404. |
| `POST /api/v1/inventory` | Validate and insert a record; duplicate names return 409. |

Four API integration tests passed: migrated-record listing, create/read-back, invalid and duplicate data handling, and missing-item handling. A live local run also returned `{"status":"ok"}` from `/health` and returned the four sample inventory records.

### Docker Compose deployment

The Compose file defines two services built from separate Dockerfiles. They share a named SQLite volume. The `db-init` service exits after initialization; exit code 0 is expected. On a subsequent run against an already populated persistent volume, it reported `Imported 0 inventory records`; the API still returned the existing four records. The API service remained up on port 8000, and the health endpoint responded successfully.

During setup, Compose initially reported that it could not find a configuration file because it was run from `C:\Users\aokoh`, not the Lab 4 folder. Running it from `Labs\Lab4`, where `docker-compose.yml` resides, resolved the issue. Docker also required Windows virtualization/WSL setup before installation could proceed.

### Screenshot placeholders

- **[SCREENSHOT PLACEHOLDER — Insert the rendered dependency diagram or the diagram source in VS Code.]**
- **[SCREENSHOT PLACEHOLDER — Insert the `docker compose up --build` output showing both images built, `db-init` completed, and the API started.]**
- **[SCREENSHOT PLACEHOLDER — Insert `docker compose ps` showing the API service running.]**
- **[SCREENSHOT PLACEHOLDER — Insert `http://localhost:8000/docs` or `/health` in a browser.]**
- **[SCREENSHOT PLACEHOLDER — Insert the inventory endpoint showing the four migrated sample records.]**

## 8. Verification summary

The following checks were run after the code was organized into lab-specific folders:

| Lab | Verification | Result |
|---|---|---|
| Lab 1 | `python app.py` | Passed; four student records and high/low score output displayed. |
| Lab 2 | `python -m unittest discover -s tests -v`; `python app.py` | Passed; 2 tests; demo displayed high, low, and median scores. |
| Lab 3 | `python -m unittest discover -s tests -v`; `python app.py` | Passed; 3 tests; inventory report displayed total value and quantity extremes. |
| Lab 4 | `python -m unittest discover -s tests -v` | Passed; 4 API integration tests. |
| Lab 4 | `docker compose up --build`; `docker compose ps`; HTTP health/list checks | Passed; API service remained running, health returned `ok`, and four inventory records were available. |

## 9. Challenges and observations

1. **Working-directory-sensitive commands:** Docker Compose looks for its configuration in the current folder. Running it from the home folder failed; running it from `Labs\Lab4` succeeded.
2. **Persistent seed data:** The database initializer is intentionally idempotent. It can import zero new rows when the named volume already contains the four records; the API list endpoint confirmed those records remained available.
3. **Windows virtualization prerequisites:** Docker installation required Windows virtualization/WSL setup. After Docker was installed, the Compose images built and the service ran.
4. **Repository consolidation:** Lab 3 already had its own Git history. Its files and CSA evidence were placed in `Labs/Lab3` for the one-repository submission, while its earlier commit identifiers are explicitly described as provenance.
5. **Evidence remains to be inserted:** The report has clearly marked image placeholders. Original screenshots must be captured by the student before a final PDF is submitted.

## 10. Conclusion

The practical demonstrates how modular code, maintenance categories, Git baselines and tags, tests, change logs, and configuration status records can support a software lifecycle. The student-score and inventory examples show defensive input/empty-data handling and separation of concerns. The final migration makes inventory data persistent in SQLite, exposes it through a tested HTTP API, and packages initialization and API execution as separate Compose services.

The code and checks are in place, but the report is still an evidence draft: screenshot placeholders must be replaced with original captures, and the consolidated change set is on the feature branch pending pull-request review. The final submission should be exported as a single PDF after screenshots and any required reviewer evidence are added.

## References and project links

- SEN 401 Lab Assessment brief supplied for this practical.
- Individual repository: [github.com/OkohAlex/sen401_scm_lab](https://github.com/OkohAlex/sen401_scm_lab).
- Consolidated folder-structure pull request: [PR #3](https://github.com/OkohAlex/sen401_scm_lab/pull/3).
- The report and implementations in this repository were prepared for this individual submission; screenshots remain to be captured by the student.
