# Lab 4: Re-engineered Inventory API

This lab separates the inventory API into Pydantic schemas, SQLite storage,
database controllers, and FastAPI routes. Sample records from the Lab 3
inventory project are migrated from `data/legacy_inventory.json` into SQLite.

## Run locally

From this directory:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-test.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m app.seed
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`; interactive endpoint
documentation is at `http://127.0.0.1:8000/docs`.

## Endpoints

- `GET /health` checks service availability.
- `GET /api/v1/inventory` lists stored items.
- `GET /api/v1/inventory/{item_id}` reads one item.
- `POST /api/v1/inventory` validates and stores an item.

SQLite is stored at `data/inventory.db` by default. Set `DATABASE_PATH` to use
a different file.

## Docker Compose

Docker Desktop is required. From this directory, build and start both services:

```powershell
cd "C:\Users\aokoh\Documents\MIVA\400L\1ST SEMESTER\SEN 401 - Software Configuration Management and Maintenance\SEN 401 Lab - Alex\individual_sen401_scm_lab\Labs\Lab4"
docker compose up --build
```

The one-shot `db-init` container imports the JSON records into a named SQLite
volume before the API container starts. The API and initializer use separate
Dockerfiles and share the persistent database volume. Stop the services with
`Ctrl+C`, then run `docker compose down` to remove containers while retaining
the volume.

`db-init` exits after doing its one-time work; an exit code of `0` is
successful. If the persistent database already contains the sample records,
the initializer may report `Imported 0 inventory records` because it avoids
duplicates. The `api` container should stay running on port `8000`. Check the
containers from another PowerShell window opened in this folder:

```powershell
docker compose ps
```

Verify the service in a browser at `http://localhost:8000/docs`,
`http://localhost:8000/health`, and
`http://localhost:8000/api/v1/inventory`. Capture your own terminal and browser
screenshots for the assessment report.

## Reverse-engineering evidence

See `docs/reverse_engineering.md` for the module analysis and
`docs/dependency_diagram.mmd` for the dependency diagram source.
