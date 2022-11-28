import allure
from selene.support.shared import browser

from asos import utils


def screenshot(*, name='screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def logs(*, name='browser_logs'):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, name=name, attachment_type=allure.attachment_type.TEXT)


def xml_dump(*, name='page xml dump'):
    allure.attach(
        browser.driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.XML,
    )


def html_dump(*, name='page html dump'):
    allure.attach(
        browser.driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )


def video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, attachment_type=allure.attachment_type.HTML)


def video_from_browserstack(session_id, *, name='video recording'):
    video_url = utils.browserstack.get.video_url(session_id=session_id)

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )
