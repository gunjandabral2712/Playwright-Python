Playwright Python POM Example
=================================

Small sample Playwright framework using Python, Pytest and the Page Object Model (POM).

Quickstart
---------

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:

```bash
playwright install
```

4. Run tests:

```bash
pytest -q
```

Files
-----

- [requirements.txt](requirements.txt)
- [pytest.ini](pytest.ini)
- [pages/base_page.py](pages/base_page.py)
- [pages/login_page.py](pages/login_page.py)
- [tests/conftest.py](tests/conftest.py)
- [tests/test_login.py](tests/test_login.py)
