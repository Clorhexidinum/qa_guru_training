from selene import have
from selene.support.shared import browser
from avito.model.pages.controls.dropdown import DropDown


class AdsPage:
    def __init__(self):
        self.type_of_housing = DropDown(browser.element('[data-marker="categoryId"]'), 'span[class^="styles-option"]')

    def assert_search_result(self, value: int):
        browser.all('[data-marker="item"]').should(have.size_greater_than(value))
        return self

    def assert_title(self, value: str):
        browser.element('h1').should(have.text(value))
        return self

    def add_product_to_favorite(self):
        browser.all('[data-marker="favorites-add"]').first().click()
        return self
