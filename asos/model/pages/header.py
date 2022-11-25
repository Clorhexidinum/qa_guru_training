from selene import have
from selene.support.shared import browser


class Header:
    def check_gender(self, value):
        browser.all('[data-testid="floornav"]').by(have.text(value)).first.click()
        return self

    def search(self, value):
        browser.element('#chrome-search').clear().type(value).press_enter()
        return self

    def clear_search(self):
        browser.element('#chrome-search').click().element('[data-testid="search-clear-button"]').click()
        return self

    def select_category(self, value):
        browser.all('[data-testid="primarynav-button"]').by(have.text(value)).first.click()
        return self

    def select_subcategory(self, value):
        browser.all('[data-testid="text-link"]').by(have.text(value)).first.click()
        return self

    def move_to_saved(self):
        browser.element('data-testid="savedItemsIcon"').click()
        return self

    def move_to_basket(self):
        browser.element('data-testid="miniBagIcon"').click()
        return self
