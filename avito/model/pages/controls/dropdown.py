from selene import have, Element
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: Element, options: str):
        self.element = element
        self.options = options

    def select(self, *categories):
        self.element.element('..').click()
        for category in categories:
            browser.all(self.options).by(
                have.text(category)
            ).first.click()
