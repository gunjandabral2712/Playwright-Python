import sys
import pathlib
import os
import json
import pytest

# Ensure project root is on sys.path so `pages` package is importable during tests
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# Load configuration from appsettings.json with environment variable overrides.
CONFIG_PATH = PROJECT_ROOT / "appsettings.json"
_CONFIG = {}
if CONFIG_PATH.exists():
    try:
        _CONFIG = json.loads(CONFIG_PATH.read_text(encoding="utf8"))
    except (json.JSONDecodeError, OSError):
        _CONFIG = {}


@pytest.fixture(scope="session")
def base_url():
    """Base URL for tests. Order of precedence:
    1. `BASE_URL` environment variable
    2. `BaseUrl` in `appsettings.json`
    3. default (https://the-internet.herokuapp.com)
    """
    return os.getenv("BASE_URL") or _CONFIG.get("BaseUrl") or "https://the-internet.herokuapp.com"


@pytest.fixture(scope="session")
def playwright_headless():
    """Whether Playwright should run headless. Can be overridden by env var `PLAYWRIGHT_HEADLESS` (true/false)."""
    env = os.getenv("PLAYWRIGHT_HEADLESS")
    if env is not None:
        return env.lower() in ("1", "true", "yes")
    return bool(_CONFIG.get("Playwright", {}).get("Headless", True))


# Explicit C#-style fixtures: session-scoped Browser, per-test Context and Page
# These override the plugin `page` fixture so tests use our controlled lifecycle.
@pytest.fixture(scope="session")
def browser_launcher(playwright, playwright_headless):
    """Session-scoped browser launcher (OneTimeSetUp/OneTimeTearDown equivalent)."""
    browser = playwright.chromium.launch(headless=playwright_headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def browser_context(browser_launcher):
    """Function-scoped browser context (SetUp/ TearDown equivalent).
    Creates a fresh context for each test to isolate storage/cookies.
    """
    context = browser_launcher.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(browser_context):
    """Function-scoped page created from `browser_context`. Overrides plugin `page`.
    Tests that accept `page` will receive this page instance.
    """
    p = browser_context.new_page()
    yield p
    p.close()
