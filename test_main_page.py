import pytest
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес   
    page.open() # открываем страницу
    page.should_be_login_page()
   
    

