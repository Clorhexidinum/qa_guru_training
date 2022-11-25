from selene import have
from selene.support.shared import browser
from asos.model.pages.controls.dropdown import DropDown


class Catalog:
    brand_dropdown = DropDown(browser.element('data-dropdown-id="brand"'), '[data-auto-id="refinementItem"]')

    def select_brand(self, value):
        self.brand_dropdown.select(value)

    def select_product(self, value):
        browser.all('data-auto-id="productTile"').by(have.text(value)).first.click()
        return self

    def add_product_to_wishlist(self, value):
        browser.all('data-auto-id="productTile"').by(have.text(value))\
            .first.element('[aria-label="Save for later"] span').click()
        return self



