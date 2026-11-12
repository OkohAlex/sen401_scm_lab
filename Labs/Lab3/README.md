# Lab 3: Configuration Status Accounting

This individual inventory project demonstrates corrective, adaptive,
perfective, and preventive maintenance together with Git-based configuration
status accounting. Its files have been consolidated into this folder so the
assessment can be submitted from one repository. The original standalone Lab 3
repository is retained as a backup; use the unified repository for submission.

## Project structure

- `app.py` displays inventory quantities and stock valuation.
- `inventory.py` contains the sample inventory records.
- `models.py` defines the validated inventory item type.
- `utils/helpers.py` contains reusable inventory calculations.
- `tests/` covers calculations and invalid inventory data.
- `status_accounting.csv` maps maintenance work to source commits recorded
  before consolidation.
- `changelog.txt` contains the Lab 3 source repository's exported Git history.

## Run

Python 3.10 or later is recommended. The application uses only the standard
library.

```powershell
python app.py
python -m unittest discover -s tests -v
```

## Version control and provenance

The inventory maintenance work was developed on a `dev` branch and tagged
`v1.0` before these files were consolidated. The commit identifiers in the
status-accounting register and source changelog belong to that Lab 3 history;
they are provenance records, not commits in the unified repository. Use the
unified repository's own Git history for evidence of the consolidated
submission.

## Capture evidence

Run the app and tests above, then capture their output and the unified
repository's actual branch/commit history. Do not present source-repository
commit identifiers as commits in the unified repository.
