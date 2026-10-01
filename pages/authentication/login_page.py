from playwright.sync_api import Page

from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'username')
        self.password_input = Input(page, 'password')
        self.login_button = Button(page, 'login-button')


