from selene import have
from selene.support.shared import browser
from avito.model.pages.controls.dropdown import DropDown


class RealEstatePage:
    def __init__(self):
        self.type_of_housing = DropDown(browser.element('[data-marker="categoryId"]'), 'span[class^="styles-option"]')
        self.type_of_deal = DropDown(browser.element('input[placeholder="Купить"]'),
                                     'span[class^="styles-optionText_size"]')
        self.housing_condition = DropDown(browser.element('input[placeholder="Вторичка, новостройки"]'),
                                          'span[class^="styles-optionText_size"]')
        self.number_of_rooms = DropDown(browser.element('[data-marker="params[549]/sticker/text"]'),
                                        'span[class^="multi-select-checkbox-list-item__text_size"]')

    def open(self):
        browser.open('/all/nedvizhimost')
        return self

    def select_type_of_housing(self, value: str):
        self.type_of_housing.select(value.capitalize())
        return self

    def select_type_of_deal(self, value: str):
        self.type_of_deal.select(value.capitalize())
        return self

    def select_housing_condition(self, value: str):
        self.housing_condition.select(value.capitalize())
        return self

    def select_number_of_rooms(self, value: str):
        self.number_of_rooms.select(value)
        return self

    def show_variants(self):
        browser.element('[data-marker="search-form-widget/action-button-0"]').click()
        return self

    def select_other_services(self, value: str):
        browser.all('div[class^="category-category"]').by(have.text(value.capitalize())).first.click()
        return self
