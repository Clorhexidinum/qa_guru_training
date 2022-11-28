from selene import have
from selene.support.shared import browser
from asos.model.pages.controls.dropdown import DropDown


class Catalog:
    def __init__(self):
        self.brand_dropdown = DropDown(browser.element('[data-dropdown-id="brand"]'), '[data-auto-id="refinementItem"]')

    def title(self):
        return browser.element('h1')

    def product_cards(self):
        return browser.all('[data-auto-id="productTile"]')

    def search_banner(self):
        return browser.element('#search-term-banner')

    def select_brand(self, value):
        self.brand_dropdown.select(value)
        return self

    def select_product(self, value):
        browser.all('[data-auto-id="productTile"]').by(have.text(value)).first.click()
        return self

    def add_product_to_saved(self):
        browser.all('[data-auto-id="productTile"]').first.element('[aria-label="Save for later"] span').click()
        return self



