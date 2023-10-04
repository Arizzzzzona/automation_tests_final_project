from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
import time
import random
import string


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #проверка на корректный url адрес
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        time.sleep(5)
        assert "login" in self.browser.current_url,"It's not Login link"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"
        

    def should_be_register_form(self):
        #проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self,email,password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        #email = self.generate_random_email
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        #password = self.generate_random_password
        input_password.send_keys(password)
        input_accept_password = self.browser.find_element(*LoginPageLocators.ACCEPT_PASSWORD)
        input_accept_password.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        btn.click()

    def generate_random_email(self):
    # Генерация случайной почты
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        email = f"{username}@{domain}.com"
        return email

    def generate_random_password(self,length=9):
        # Генерация случайного пароля
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password