# SEN 401 Software Configuration Management Lab

**Submission type:** Individual  
**Student:** Okoh Edache Alex  
**Matric number:** 2023/C/SENG/0389  
**Repository:** [OkohAlex/sen401_scm_lab](https://github.com/OkohAlex/sen401_scm_lab)

This repository organizes the practical assessment into one folder per lab.
Each lab has its own instructions, source files, dependencies, and tests where
applicable. Screenshots and final report evidence should be captured from this
individual project and added only after the work has been verified.

## Labs

| Folder | Assessment work | Start here |
|---|---|---|
| [`Labs/Lab1/`](Labs/Lab1/) | Modular student demo, Git baseline, and release `v1.0` | [`Labs/Lab1/README.md`](Labs/Lab1/README.md) |
| [`Labs/Lab2/`](Labs/Lab2/) | Student application maintenance, regression tests, and release `v1.1` | [`Labs/Lab2/README.md`](Labs/Lab2/README.md) |
| [`Labs/Lab3/`](Labs/Lab3/) | Inventory maintenance, Git changelog, and configuration status accounting | [`Labs/Lab3/README.md`](Labs/Lab3/README.md) |
| [`Labs/Lab4/`](Labs/Lab4/) | Reverse engineering, FastAPI, SQLite migration, and Docker Compose | [`Labs/Lab4/README.md`](Labs/Lab4/README.md) |

## Running the Python labs

Run commands from the corresponding lab folder so Python imports resolve to
that lab's modules rather than another lab's files.

```powershell
cd Labs\Lab1
python app.py
```

Labs 2 and 3 include tests. For example:

```powershell
cd Labs\Lab2
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python app.py
```

Use the individual README in each folder for its complete setup and verification
commands. Lab 4 requires Docker Desktop; run Compose from `Labs\Lab4`.

## Version control

The Git history contains the starter baseline and maintenance work. Lab 1 uses
the `v1.0` tag; Lab 2 uses `v1.1`. Lab 4 changes are proposed through a pull
request. Refer to the actual GitHub branches and commit history when capturing
version-control evidence.

## Evidence and academic integrity

Take original screenshots from this repository, its local program output, and
your own GitHub history. Do not reuse another student's screenshots or report
text. Add the screenshots to your report only after you have personally
verified the corresponding commands and results.
