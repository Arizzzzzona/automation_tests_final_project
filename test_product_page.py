from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser,link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес   
    page.open() # открываем страницу
    page.add_to_basket()
    time.sleep(5)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
    


def test_guest_cant_see_success_message(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_disapered()

def test_guest_should_see_login_link_on_product_page(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser,link)
    page.open()
    page.basket_should_be_empty()



class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="class",autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.login_page = LoginPage(browser,link)
        self.login_page.open()
        self.login_page.register_new_user(self.login_page.generate_random_email(),self.login_page.generate_random_password())
        time.sleep(5)
        self.login_page.should_be_authorized_user()
    
    
    def test_user_cant_see_success_message(self,browser):
        
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser,link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес   
        page.open() # открываем страницу
        page.add_to_basket()
