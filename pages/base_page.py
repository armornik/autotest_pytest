from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
import math

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url: str, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        """Open link in browser"""
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        """Check if an element is on the page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self) -> None:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        """Check for missing element on page"""
        try:
            WebDriverWait(self.browser, timeout).until(e_c.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(e_c.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self) -> None:
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self) -> None:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
