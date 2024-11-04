from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    SIGN_UP_LINK = (By.XPATH, '//a[@href="/register"]')  # Ссылка на регистрацию
    INPUT_NAME = (By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input[@name="name"]')  # Поле ввода имени
    INPUT_EMAIL = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input[@name="name"]')  # Поле ввода почты
    INPUT_PASSWORD = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input[@name="Пароль"]')  # Поле ввода пароля
    SIGN_UP_BTN = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    SIGN_IN_BTN = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"
    SIGN_TO_ACCOUNT_BTN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт"
    SIGN_IN_TITLE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок "Вход"
    ERROR_WRONG_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Ошибка "Некорректный пароль"
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"
    SIGN_IN_LINK = (By.XPATH, '//a[@href="/login"]')  # Ссылка на вход
    CONSTRUCTOR_BTN = (By.XPATH, '//a[@href="/"]')  # Кнопка перехода на страницу конструктора
    LOGO_BTN = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Кнопка перехода на главную страницу
    PROFILE_LINK = (By.XPATH, '//a[@href="/account/profile"]')  # Ссылка на личный кабинет
    SIGN_OUT_BTN = (By.XPATH, '//button[text()="Выход"]')   # Кнопка "Выход"
    SAUCE_LINK = (By.XPATH, '//span[text()="Соусы"]')   # Ссылка "Соусы"
    FILLINGS_LINK = (By.XPATH, '//span[text()="Начинки"]')   # Ссылка "Начинки"
    BUNS_LINK = (By.XPATH, '//span[text()="Булки"]')   # Ссылка "Булки"
    CURRENT_MENU_LINK = (By.CLASS_NAME, 'tab_tab_type_current__2BEPc')  # Выбранный раздел меню