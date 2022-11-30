import allure
import pytest
from avito.model.pages import header, real_estate_page, ads_page, favorite_page

header = header.Header()
real_estate = real_estate_page.RealEstatePage()
ads = ads_page.AdsPage()
favotite = favorite_page.FavoritePage()


# @allure.feature('Navigation')
# @allure.suite('Header')
# @allure.tag('ui', 'nav', 'positive')
# @allure.label("owner", "Murat Kubekov")
# @allure.title('Открытие страницы каталога')
# @pytest.mark.parametrize('category', ['недвижимость', 'услуги', 'личные вещи'])
# def test_open_catalog(category):
#     with allure.step(f'Открыть страницу {category}'):
#         header.select_category(category.upper())
#
#     with allure.step('Проверить заголовок'):
#         ads.assert_title(category.capitalize())
#
#
# @allure.feature('Navigation')
# @allure.suite('Header')
# @allure.tag('ui', 'nav', 'positive')
# @allure.label("owner", "Murat Kubekov")
# @allure.title('Открытие страницы каталога c выбранным городом')
# @pytest.mark.parametrize('category', ['недвижимость', 'услуги', 'личные вещи'])
# def test_open_catalog_with_select_sity(category):
#     with allure.step(f'Открыть страницу {category}'):
#         header.select_category(category.upper()).select_region('Москва')
#
#     with allure.step('Проверить заголовок'):
#         ads.assert_title(f'{category.capitalize()} в Москве')
#
#
# @allure.feature('Filter')
# @allure.suite('Nedvizhimost page')
# @allure.tag('ui', 'filter', 'positive')
# @allure.label("owner", "Murat Kubekov")
# @allure.title('Работа фильтра на странице недвижимость')
# @pytest.mark.parametrize('house', ['квартира', 'комната'])
# @pytest.mark.parametrize('deal', ['купить', 'снять'])
# def test_filter_selection(house, deal):
#     with allure.step('Открыть страницу недвижимости'):
#         real_estate.open()
#
#     with allure.step(f'Установить фильтр {house} {deal}'):
#         real_estate \
#             .select_type_of_housing(house) \
#             .select_type_of_deal(deal) \
#             .show_variants()
#
#     with allure.step(f'Проверить результат поиска'):
#         ads.assert_search_result(1)
#
#
# @allure.feature('Search')
# @allure.suite('Header')
# @allure.tag('ui', 'search', 'positive')
# @allure.label("owner", "Murat Kubekov")
# @allure.title('Поиск продукта с главной страницы')
# @pytest.mark.parametrize("value", ['куртка', 'шапка', 'ботинки'])
# def test_search_product(value):
#     with allure.step(f'Поиск продукта {value}'):
#         header \
#             .search(value) \
#             .search_submit()
#
#     with allure.step('Проверить заголовок сраницы и найденные элементы'):
#         ads \
#             .assert_title(f'Объявления по запросу «{value}»') \
#             .assert_search_result(0)
#
#
# @allure.feature('Save product')
# @allure.suite('Ads page')
# @allure.tag('ui', 'save', 'positive')
# @allure.label("owner", "Murat Kubekov")
# @allure.title('Добавление в избранное со странцы объявлений')
# @pytest.mark.parametrize("value", ['куртка', 'шапка', 'ботинки'])
# def test_add_to_saved_on_the_ads_page(value):
#     with allure.step(f'Поиск продукта {value}'):
#         header \
#             .search(value) \
#             .search_submit()
#
#     with allure.step('Добавляем в избранное'):
#         ads.add_product_to_favorite()
#
#     with allure.step('Переходим в избранное'):
#         header.move_to_favourites()
#         favotite.assert_saved_result(0)

@allure.feature('Navigation')
@allure.suite('Header')
@allure.tag('ui', 'nav', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Открытие страницы каталога')
@pytest.mark.parametrize('category', ['недвижимость', 'услуги', 'личные вещи'])
def test_open_catalog(category):
    with allure.step(f'Открыть страницу'):
        header.select_category('НЕДВИЖИМОСТЬ')

    with allure.step('Проверить заголовок'):
        ads.assert_title('Недвижимость')


@allure.feature('Navigation')
@allure.suite('Header')
@allure.tag('ui', 'nav', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Открытие страницы каталога c выбранным городом')
@pytest.mark.parametrize('category', ['недвижимость', 'услуги', 'личные вещи'])
def test_open_catalog_with_select_sity():
    with allure.step(f'Открыть страницу'):
        header.select_category('НЕДВИЖИМОСТЬ').select_region('Москва')

    with allure.step('Проверить заголовок'):
        ads.assert_title(f'Недвижимость в Москве')


@allure.feature('Filter')
@allure.suite('Nedvizhimost page')
@allure.tag('ui', 'filter', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Работа фильтра на странице недвижимость')
# @pytest.mark.parametrize('house', ['квартира', 'комната'])
# @pytest.mark.parametrize('deal', ['купить', 'снять'])
def test_filter_selection():
    with allure.step('Открыть страницу недвижимости'):
        real_estate.open()

    with allure.step(f'Установить фильтр '):
        real_estate \
            .select_type_of_housing('квартира') \
            .select_type_of_deal('купить') \
            .show_variants()

    with allure.step(f'Проверить результат поиска'):
        ads.assert_search_result(1)


@allure.feature('Search')
@allure.suite('Header')
@allure.tag('ui', 'search', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Поиск продукта с главной страницы')
# @pytest.mark.parametrize("value", ['куртка', 'шапка', 'ботинки'])
def test_search_product():
    with allure.step(f'Поиск продукта'):
        header \
            .search('куртка') \
            .search_submit()

    with allure.step('Проверить заголовок сраницы и найденные элементы'):
        ads \
            .assert_title(f'Объявления по запросу «куртка»') \
            .assert_search_result(0)


@allure.feature('Save product')
@allure.suite('Ads page')
@allure.tag('ui', 'save', 'positive')
@allure.label("owner", "Murat Kubekov")
@allure.title('Добавление в избранное со странцы объявлений')
# @pytest.mark.parametrize("value", ['куртка', 'шапка', 'ботинки'])
def test_add_to_saved_on_the_ads_page():
    with allure.step(f'Поиск продукта'):
        header \
            .search('куртка') \
            .search_submit()

    with allure.step('Добавляем в избранное'):
        ads.add_product_to_favorite()

    with allure.step('Переходим в избранное'):
        header.move_to_favourites()
        favotite.assert_saved_result(0)
