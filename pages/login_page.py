from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    RESTORE_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")
    LOGIN_INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/../input"]  # Вход поле Email
    LOGIN_INPUT_PASSWORD = [By.XPATH, ".//label[text()='Пароль']/../input"]  # Вход поле Пароль
    LOG_ON_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Войти']"]

    @allure.step("Клик на Восстановить пароль")
    def click_restore_password(self):
        self.click(self.RESTORE_PASSWORD)

    @allure.step("Авторизация в личном кабинете")
    def login(self, email, password):
        self.click(self.LOGIN_INPUT_EMAIL)
        self.send_input(self.LOGIN_INPUT_EMAIL, email)
        self.click(self.LOGIN_INPUT_PASSWORD)
        self.send_input(self.LOGIN_INPUT_PASSWORD, password)
        self.click(self.LOG_ON_BUTTON)

    @allure.step("Поиск кнопки Войти")
    def check_login_button(self):
        return self.find_element(self.LOG_ON_BUTTON)
