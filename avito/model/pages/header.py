from selene import have
from selene.support.shared import browser
from avito.model.pages.controls.dropdown import DropDown


class Header:
    def __init__(self):
        self.category = DropDown(browser.element('#category'), 'option')

    def open(self):
        browser.open('')
        return self

    def select_category(self, value):
        self.category.select(value)
        return self

    def search(self, value):
        browser.element('#downshift-input').type(value).press_enter()
        return self

    def select_region(self, value):
        browser.element('[data-marker="search-form/region"]').click()
        browser.element('[data-marker="popup-location/region/input"]').type(value)
        browser.element('[data-marker="popup-location/save-button"]').click()
        return self

    def search_submit(self):
        browser.element('[data-marker="search-form/submit-button"]').click()
        return self

    def move_to_favourites(self):
        browser.element('[title="Избранное"]').click()
        return self

    def open_product(self):
        browser.element('[itemtype="http://schema.org/Product"]').first().click()
        return self

