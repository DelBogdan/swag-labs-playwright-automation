from playwright.sync_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):

    # Проверки элемента Input

    def check_have_value(self, value: str, nth: int = 0):
        locator = self.get_locator(nth)
        expect(locator).to_have_value(value)