import allure
import pytest
from selene import have
from selene.support.shared import browser

from asos.model.pages.catalog import Catalog
from asos.model.pages.header import Main
from asos.model.pages.product import Product

main_page = Main()
catalog = Catalog()
product = Product()


@allure.feature('Navigation')
@allure.suite('Catalog page')
@allure.tag('ui', 'nav', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Open catalog page')
@pytest.mark.parametrize('gender', ['men', 'women'])
@pytest.mark.parametrize('product_type', ['boots', 'trainers'])
def test_open_catalog(setup_browser, gender, product_type):
    with allure.step(f'Opening the {product_type} page'):
        main_page \
            .check_gender(gender) \
            .select_category('shoes') \
            .select_subcategory(product_type)

    with allure.step('Check the title and the availability of goods'):
        catalog.title().should(have.text(f"{gender.capitalize()}'s {product_type.capitalize()}"))
        catalog.product_cards().should(have.size_greater_than(0))


@allure.feature('Filter')
@allure.suite('Catalog page')
@allure.tag('ui', 'filter', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Select brand on catalog page')
@pytest.mark.parametrize('brand', ['ASOS DESIGN', 'ASOS 4505'])
def test_brand_selection(brand):
    with allure.step('Оpening the catalog page'):
        main_page \
            .check_gender('men') \
            .select_category('clothing') \
            .select_subcategory('shirts')

    with allure.step(f'Select brand {brand}'):
        catalog \
            .select_brand(brand) \
            .product_cards().should(have.size_greater_than(0))


@allure.feature('Search')
@allure.suite('Main page')
@allure.tag('ui', 'search', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Search product product on main page')
@pytest.mark.parametrize("value", ['shirts', 'shorts', 'socks'])
def test_search_product(value):
    with allure.step(f'Search product {value}'):
        main_page.given_opened().search(value)

    with allure.step('Check the title and the availability of goods'):
        catalog \
            .search_banner().should(have.text(value.capitalize())) \
            .product_cards().should(have.size_greater_than(0))


@allure.feature('Save product')
@allure.suite('Catalog page')
@allure.tag('ui', 'save', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Add to saved on the catalog page')
def test_add_to_saved_on_the_catalog_page():
    with allure.step('Search product'):
        main_page.search('shirts')

    with allure.step('Open product card'):
        catalog.add_product_to_saved()

    with allure.step('Check that the product is saved'):
        main_page.move_to_saved()
        browser.all('#saved-lists-app li').should(have.size(1))


@allure.feature('Save product')
@allure.suite('Product page')
@allure.tag('ui', 'save', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Add to saved on the product page')
def test_add_product_to_saved():
    with allure.step('Search product'):
        main_page.search('shirts')

    with allure.step('Open product card'):
        catalog.select_product('')

    with allure.step('Add product to saved'):
        product \
            .select_size('UK 8') \
            .add_to_wishlist()

    with allure.step('Check that the product is saved'):
        main_page.move_to_saved()
        browser.all('#saved-lists-app li').should(have.size(1))


@allure.feature('Bag')
@allure.suite('Product page')
@allure.tag('ui', 'bag', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Add to bag on the product page')
def test_add_product_to_bag():
    with allure.step('Search product'):
        main_page.search('shirts')

    with allure.step('Open product card'):
        catalog.select_product('')

    with allure.step('Add product to saved'):
        product \
            .select_size('UK 8') \
            .add_to_bag()

    with allure.step('Check that the product is saved'):
        browser.all('#sminibag-dropdown li').should(have.size(1))
