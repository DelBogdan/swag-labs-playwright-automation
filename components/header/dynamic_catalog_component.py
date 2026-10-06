from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.header.dynamic_catalog_submenu_component import DynamicCatalogSubmenuComponent
from elements.link import Link


class DynamicCatalogComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dynamic_catalog_sidebar_link = Link(page, 'dynamic-catalog-sidebar-link')

        self.dynamic_catalog_submenu_component = DynamicCatalogSubmenuComponent(page)

    def check_visible(self):
        self.dynamic_catalog_sidebar_link.check_visible()
        self.dynamic_catalog_submenu_component.check_visible()