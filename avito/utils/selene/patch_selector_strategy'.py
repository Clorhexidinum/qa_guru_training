from typing import Union, Tuple

from appium.webdriver.common.appiumby import AppiumBy
from selene import Browser
from selene.core.entity import Element, Collection
import re

from avito.utils.python import monkey


def is_word_with_dashes_underscores_or_numbers(selector):
    return re.match(r'^[a-zA-Z_\d\-]+$', selector)


def are_words_with_dashes_underscores_or_numbers_separated_by_space(selector):
    return re.match(r'^[a-zA-Z_\d\- ]+$', selector)


def _by(selector: str | Tuple[str, str]):
    if isinstance(selector, tuple):
        return selector

    if selector.startswith('#') and is_word_with_dashes_underscores_or_numbers(
        selector[1:]
    ):
        appName = 'org.wikipedia.alpha'
        return AppiumBy.ID, f'{appName}:id/{selector[1:]}' if appName else selector[1:]

    if are_words_with_dashes_underscores_or_numbers_separated_by_space(selector):
        return AppiumBy.ACCESSIBILITY_ID, selector

    raise Exception(f'Unsupported selector: {selector}')


original_browser_element = Browser.element  # сохраняем старую версию элемента


@monkey.patch_method_in(Browser)
def element(self, selector: Union[str, tuple]) -> Element:
    return original_browser_element(self, _by(selector))


original_browser_all = Browser.all # сохраняем старую версию


@monkey.patch_method_in(Browser)
def all(self, selector: Union[str, tuple]) -> Collection:
    return original_browser_all(self, _by(selector))


original_element_element = Element.element