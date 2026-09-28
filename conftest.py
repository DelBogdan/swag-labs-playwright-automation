import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def get_browser():
    """
    Фикстура, которая открывает выбранный браузер для всех автотестов.
    По завершению тестов, закрывает браузер.
    :return: Возращает объект типа Browser
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def get_public_context(get_browser):
    """
    Возвращает публичный контекст, полностью изолированный на каждый тест.
    После завершения теста, закрывает контекст.
    :param get_browser: Используем фикстуру получения браузера, чтобы работать с контекстом.
    :return: Возвращает объект типа Context
    """
    context = get_browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope='function')
def get_public_page(get_public_context):
    """
    Возвращает публичную страницу используя контекст в каждый тест. После завершения теста закрывает страниу.
    :param get_public_context: Использует публичный контекст.
    :return: Возвращает объект типа Page
    """
    page = get_public_context.new_page()
    yield page
    page.close()
