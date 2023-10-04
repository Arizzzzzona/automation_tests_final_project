from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):

    def basket_should_be_empty(self):
        self.go_to_basket_page()
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket not empty"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "should contains message"
