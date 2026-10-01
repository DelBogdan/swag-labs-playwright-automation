from typing import Union

from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: Union[str, Locator]):
        self.page = page
        self.locator = locator

    # Получить локатор

    def get_locator(self, nth: int = 0) -> Locator:
        """
        Данный метод возвращает локатор. Если передана строка,
        то вернет через get_by_test_id, если у какого-то элемента нет атрибута
        data_testid, то в классе странице создадим локатор вручную и передадим сюда

        :return: Возвращает объект типа Locator
        """
        if isinstance(self.locator, str):
            base_locator = self.page.get_by_test_id(self.locator)
        else:
            base_locator = self.locator
        return base_locator.nth(nth)

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
