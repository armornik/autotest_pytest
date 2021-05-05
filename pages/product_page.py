from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self) -> None:
        self.add_to_cart()
        self.should_be_present_in_cart()
        self.should_check_overall_cost()

    def add_to_cart(self) -> None:
        """Check button 'Add to basket' on the page, and click if button exist"""
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button add to basket is not presented"
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_CART).click()
        self.solve_quiz_and_get_code()

    def should_be_present_in_cart(self) -> None:
        """Check name product with name product from basket"""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_CART
        ), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def should_check_overall_cost(self) -> None:
        """Check price in product from basket and page"""
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS
                                       ), "No alert with cart status"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
