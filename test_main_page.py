# pytest -s -v --tb=line --language=en test_main_page.py
# pytest -s -m "login_guest" test_main_page.py
from selenium.webdriver import Remote as RemoteWebDriver
import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser: RemoteWebDriver) -> None:
        """Check test use command 'pytest -v --tb=line --language=en test_main_page.py'"""
        link = "http://selenium1py.pythonanywhere.com/"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        page = MainPage(browser, link)  # init Page Object, pass the driver instance to the constructor and url address
        page.open()  # open page
        page.go_to_login_page()  # execute the page method - go to the login page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser: RemoteWebDriver) -> None:
        """Check login link"""
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: RemoteWebDriver) -> None:
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.should_be_basket_empty()


