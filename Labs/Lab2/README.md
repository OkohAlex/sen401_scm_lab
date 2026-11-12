# Lab 2: Software Maintenance

This individual lab applies corrective, adaptive, perfective, and preventive
maintenance to the Lab 1 student application.

## Changes by maintenance type

- **Corrective:** empty student cohorts are handled without an exception;
  score helpers return `None` when no record exists.
- **Adaptive:** Pydantic validates non-empty student names and scores in the
  0–100 range.
- **Perfective:** the console app reports highest, lowest, and median scores.
- **Preventive:** responsibilities are separated into `students.py`,
  `utils/helpers.py`, and `app.py`, with type hints, docstrings, and regression
  tests.

## Files

- `students.py` defines the validated student model and sample records.
- `utils/helpers.py` implements highest, lowest, and median calculations.
- `app.py` displays the records and cohort statistics.
- `tests/test_helpers.py` checks empty and populated cohorts.
- `requirements.txt` lists Pydantic.

## Run and test

From this directory:

```powershell
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python app.py
```

The maintenance changes were developed on the repository's `maintenance`
branch and released with tag `v1.1`. Capture the branch, commits, tag, passing
tests, and console output as your own report evidence.
