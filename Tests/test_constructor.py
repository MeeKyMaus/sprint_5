from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import setup_driver


class TestBunsSection:
    # Тест перехода к разделу "Булки"
    def test_go_to_buns_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        buns_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUNS_LINK))
        buns_link.click()

        current_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CURRENT_MENU_LINK))
        assert current_section.text == "Булки"


class TestSaucesSection:
    # Тест перехода к разделу "Соусы"
    def test_go_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        sauces_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCE_LINK))
        sauces_link.click()

        current_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CURRENT_MENU_LINK))
        assert current_section.text == "Соусы"


class TestFillingsSection:
    # Тест перехода к разделу "Начинки"
    def test_go_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        fillings_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_LINK))
        fillings_link.click()

        current_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CURRENT_MENU_LINK))
        assert current_section.text == "Начинки"

