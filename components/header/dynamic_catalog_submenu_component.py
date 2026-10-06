from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.link import Link


class DynamicCatalogSubmenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.lazy_load_link = Link(page, 'dynamic-catalog-lazy-load-link')
        self.spinner_link = Link(page, 'dynamic-catalog-spinner-link')
        self.slider_link = Link(page, 'dynamic-catalog-slider-link')

    def check_visible(self):
        self.lazy_load_link.check_visible()
        self.spinner_link.check_visible()
        self.slider_link.check_visible()