from selene import have
from selene.support.shared import browser
from avito.model.pages.controls.dropdown import DropDown


class FavoritePage:
    def __init__(self):
        self.type_of_housing = DropDown(browser.element('[data-marker="categoryId"]'), 'span[class^="styles-option"]')

    def assert_saved_result(self, value: int):
        browser.all('[class^="item-snippet-root"]').should(have.size_greater_than(value))
        return self
