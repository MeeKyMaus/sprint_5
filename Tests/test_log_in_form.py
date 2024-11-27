import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin:
    # Тест входа по кнопке "Войти в аккаунт" на главной
    def test_login_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SIGN_TO_ACCOUNT_BTN))
        login_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_IN_TITLE))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    # Тест входа через кнопку "Личный кабинет"
    def test_login_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        personal_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BTN))
        personal_account_button.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SIGN_IN_TITLE))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


