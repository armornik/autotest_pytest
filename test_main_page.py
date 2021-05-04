from selenium.webdriver import Remote as RemoteWebDriver

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser: RemoteWebDriver):
    """Check test use command 'pytest -v --tb=line --language=en test_main_page.py'"""
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # init Page Object, pass the driver instance to the constructor and url address
    page.open()                      # open page
    page.go_to_login_page()          # execute the page method - go to the login page


def test_guest_should_see_login_link(browser: RemoteWebDriver):
    """Check login link"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
