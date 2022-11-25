from selene import have, Element
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: Element, options: str):
        self.element = element
        self.options = options

    def select(self, option):
        self.element.click()
        browser.all(self.options).by(
            have.exact_text(option)
        ).first.click()
