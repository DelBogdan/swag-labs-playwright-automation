from playwright.sync_api import Page

from components.header.dynamic_catalog_component import DynamicCatalogComponent
from elements.button import Button

from components.base_component import BaseComponent
from elements.link import Link


class BurgerMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.close_menu_button = Button(page, 'close-menu')
        self.all_items_link = Link(page, 'inventory-sidebar-link')

        self.dynamic_catalog_component = DynamicCatalogComponent(page)

        self.logout_link = Link(page, 'logout-sidebar-link')
        self.reset_app_state_link = Link(page, 'reset-sidebar-link')

    def check_visible(self):
        """
        Здесь видимость компонента сработает только если был
        клик по кнопке Dynamic Catalog
        """
        self.close_menu_button.check_visible()
        self.all_items_link.check_visible()
        self.dynamic_catalog_component.check_visible()
        self.logout_link.check_visible()
        self.reset_app_state_link.check_visible()