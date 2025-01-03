import pytest
from selenium import webdriver

@pytest.fixture
def setup_driver():
    # Открываем браузер
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    # Закрываем браузер после теста
    driver.quit()



