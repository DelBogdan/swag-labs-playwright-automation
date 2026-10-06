from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.header.burger_menu_component import BurgerMenuComponent
from elements.button import Button
from elements.link import Link
from elements.select import Select
from elements.text import Text


class Header(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'title')

        locator_burger_menu_button = page.locator("//button[@id='react-burger-menu-btn']")
        self.burger_menu_button = Button(page, locator_burger_menu_button)

        self.burger_menu_component = BurgerMenuComponent(page)

        self.shopping_cart_link = Link(page, 'shopping-cart-link')
        self.product_sort_container = Select(page, 'product-sort-container')