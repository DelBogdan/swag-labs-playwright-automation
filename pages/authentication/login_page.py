import re

from playwright.sync_api import Page

from components.authentication.error_message_form import ErrorMessageForm
from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.error_component = ErrorMessageForm(page)

        self.email_input = Input(page, 'username')
        self.password_input = Input(page, 'password')
        self.login_button = Button(page, 'login-button')

    def click_login_button(self):
        self.login_button.click()
        self.check_current_url(re.compile(r".*/inventory.html"))

    def check_visible_wrong_email_or_password_alert(self, text: str):
        self.error_component.check_visible(text)



