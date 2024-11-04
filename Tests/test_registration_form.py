import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Тест успешной регистрации
@pytest.mark.parametrize("name, email, password", [
    ("TestUser11", "zakharchornyy16@yandex.ru", "123456")
])
def test_successful_registration(driver, name, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INPUT_NAME))
    email_field = driver.find_element(*Locators.INPUT_EMAIL)
    password_field = driver.find_element(*Locators.INPUT_PASSWORD)

    name_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    register_button = driver.find_element(*Locators.SIGN_UP_BTN)
    register_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


# Тест на ошибку при некорректном пароле
@pytest.mark.parametrize("name, email, password", [
    ("TestUser1", "1234567@ya.ru", "123")
])
def test_invalid_password_registration(driver, name, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INPUT_NAME))
    email_field = driver.find_element(*Locators.INPUT_EMAIL)
    password_field = driver.find_element(*Locators.INPUT_PASSWORD)

    name_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    register_button = driver.find_element(*Locators.SIGN_UP_BTN)
    register_button.click()

    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_WRONG_PASSWORD))
    assert "Некорректный пароль" in error_message.text