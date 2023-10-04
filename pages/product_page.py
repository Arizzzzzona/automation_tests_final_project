from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    
    def add_to_basket(self):
        btn1 = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn1.click()
        self.solve_quiz_and_get_code()
        
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        text_price = price.text
        price_in_bskt = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        text_bskt_price = price_in_bskt.text
        assert text_price == text_bskt_price, 'incorrect price'

        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        text_book_name = book_name.text
        book_name_in_bskt = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        text_book_name_in_bskt = book_name_in_bskt.text
        assert text_book_name == text_book_name_in_bskt, 'incorect name'

       
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


    def should_disapered(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Succsess message is desapered"