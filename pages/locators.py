from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    # BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    # MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    # PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    # MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    # PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
