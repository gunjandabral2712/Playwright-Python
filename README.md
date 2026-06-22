Playwright Python POM Example
=============================

Small sample Playwright framework using Python, Pytest and the Page Object Model (POM).

Quickstart
----------

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:

```bash
python -m playwright install
```

Test layout and runnable commands
--------------------------------

This repository separates UI (Playwright) tests and API tests:

- UI tests: `tests/ui/` — Playwright + Pytest using the `page` fixture
- API tests: `tests/api/` — `requests`-based tests and fixtures

Run only UI tests (headless by default):

```bash
pytest tests/ui -q
```

Run UI tests headed (visible browser):

```bash
pytest --headed tests/ui -q
```

Run only API tests:

```bash
pytest tests/api -q
```

Run everything:

```bash
pytest -q
```

Configuration / environment variables
-------------------------------------

- `BASE_URL` — override the UI tests base URL (defaults to https://the-internet.herokuapp.com)
- `PLAYWRIGHT_HEADLESS` — override headless mode (true/false). The CI workflow sets this to `true`.
- `API_BASE_URL` — override the base URL used by API tests (defaults to https://jsonplaceholder.typicode.com)

Example: run UI tests headed against a custom URL

```bash
BASE_URL=https://the-internet.herokuapp.com PLAYWRIGHT_HEADLESS=false pytest --headed tests/ui -q
```

Key files
---------

- [requirements.txt](requirements.txt)
- [pytest.ini](pytest.ini)
- [appsettings.json](appsettings.json)
- `pages/login_page.py` — Page Object for the sample login flow
- [tests/conftest.py](tests/conftest.py) — shared fixtures for UI tests
- `tests/ui/` — Playwright UI tests
- `tests/api/` — requests-based API tests

CI
--

The GitHub Actions workflow runs the tests headless by default (sets `PLAYWRIGHT_HEADLESS=true`).
