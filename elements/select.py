from elements.base_element import BaseElement


class Select(BaseElement):
    def select_by_value(self, value: str, nth: int = 0):
        """Выбор опции по атрибуту value"""
        locator = self.get_locator(nth)
        locator.select_option(value=value)
        # Можно добавить логирование или ожидание здесь, если нужно

    def select_by_label(self, label: str, nth: int = 0):
        """Выбор опции по видимому тексту"""
        locator = self.get_locator(nth)
        locator.select_option(label=label)

    def select_by_index(self, index: int, nth: int = 0):
        """Выбор опции по индексу (начинается с 0)"""
        locator = self.get_locator(nth)
        locator.select_option(index=index)