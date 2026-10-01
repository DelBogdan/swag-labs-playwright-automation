from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str):
        self.page = page
        self.locator = locator

    # Получить локатор

    def get_locator(self, nth: int = 0) -> Locator:
        return self.page.get_by_test_id(self.locator).nth(nth)

    # Действия над элементами

    def click(self, nth: int = 0):
        self.get_locator(nth).click()

    def fill(self, value: str, nth: int = 0):
        self.get_locator(nth).fill(value)

    # Проверки элементов

    def check_visible(self, nth: int = 0):
        locator = self.get_locator(nth)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0):
        locator = self.get_locator(nth)
        expect(locator).to_have_text(text)
