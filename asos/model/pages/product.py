from selene.support.shared import browser
from asos.model.pages.controls.dropdown import DropDown


class Product:
    size_dropdown = DropDown(browser.element('[data-id="sizeSelect"]'), 'option')

    def select_size(self, value):
        self.size_dropdown.select(value)
        return self

    def add_to_wishlist(self):
        browser.element('[data-test-id="saveForLater"]').click()
        return self

    def add_to_bag(self):
        browser.element('#product-add-button').click()
        return self



