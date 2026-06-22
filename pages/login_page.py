DEFAULT_BASE_URL = "https://the-internet.herokuapp.com"


class LoginPage:
    """Page object for the login page using composition (no inheritance).

    Usage:
        login = LoginPage(page, base_url=base_url)
        login.goto()
        login.login(...)
    """

    PATH = "/login"

    def __init__(self, page, base_url: str = None):
        self.page = page
        if base_url:
            self.base_url = base_url.rstrip("/")
        else:
            self.base_url = DEFAULT_BASE_URL

    def goto(self, path: str = ""):
        target = self.PATH if not path else path
        url = f"{self.base_url}{target}"
        self.page.goto(url)

    # Locators
    @property
    def username_input(self):
        return self.page.locator('#username')

    @property
    def password_input(self):
        return self.page.locator('#password')

    @property
    def submit_button(self):
        return self.page.locator('button[type="submit"]')

    @property
    def flash(self):
        return self.page.locator('#flash')

    # Actions
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def has_success_message(self) -> bool:
        return self.flash.is_visible() and "You logged into a secure area!" in (self.flash.text_content() or "")

    def has_error_message(self) -> bool:
        text = self.flash.text_content() or ""
        return self.flash.is_visible() and ("Your username is invalid!" in text or "Your password is invalid!" in text)
