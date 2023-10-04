from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR,"#id_registration-password1")
    ACCEPT_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTRATION_BTN = (By.CSS_SELECTOR,"#register_form > button")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.XPATH,"//*[contains(@class, 'btn btn-lg btn-primary btn-add-to-basket')]")
    BOOK_PRICE = (By.CSS_SELECTOR,"div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR,"div.alertinner > p > strong")
    BOOK_NAME = (By.CSS_SELECTOR,"div.col-sm-6.product_main > h1")
    BOOK_NAME_IN_BASKET = (By.XPATH,"(//strong)[4]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(2) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    BASKET_BTN = (By.XPATH,"//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.XPATH,"//*[@id='content_inner']/p/a")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR," div.basket-mini.pull-right.hidden-xs > span > a")
