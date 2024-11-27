from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import setup_driver


class TestLogout:
    # Тест выхода из аккаунта
    def test_logout_from_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))
        password_field = driver.find_element(*Locators.INPUT_PASSWORD)

        email_field.send_keys("zakharchornyy16@yandex.ru")
        password_field.send_keys("123456")

        login_button = driver.find_element(*Locators.SIGN_IN_BTN)
        login_button.click()

        personal_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BTN))
        personal_account_button.click()

        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SIGN_OUT_BTN))
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


class TestConstructorNavigation:
    # Тест перехода в конструктор
    def test_go_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        constructor_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BTN))
        constructor_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


class TestLogoNavigation:
    # Тест перехода по логотипу Stellar Burgers
    def test_go_to_main_page_by_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/account")

        logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGO_BTN))
        logo.click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
