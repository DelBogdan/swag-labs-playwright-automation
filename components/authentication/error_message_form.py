from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class ErrorMessageForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'error')
        self.error_button = Button(page, 'error-button')

    def check_visible(self, text: str):
        self.title.check_visible()
        self.error_button.check_visible()

        self.title.check_have_text(text)

    def check_not_visible(self):
        expect(self.title).not_to_be_visible()
        expect(self.error_button).not_to_be_visible()
