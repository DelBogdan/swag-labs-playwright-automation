from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):

    # Проверки элемента Button

    def check_enabled(self, nth: int = 0):
        locator = self.get_locator(nth)
        expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0):
        locator = self.get_locator(nth)
        expect(locator).to_be_disabled()