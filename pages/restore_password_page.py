import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RestorePage(BasePage):
    RESTORE_PASSWORD_TEXT = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    RESTORE_EMAIL_INPUT = [By.XPATH, '//*[@class="text input__textfield text_type_main-default"]']
    RESTORE_BUTTON = [By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                      "button_button_size_medium__3zxIa' and text() = 'Восстановить']"]
    CODE_INPUT = [By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default"]']
    RESTORE_PASSWORD_ACTIVE_INPUT = [By.XPATH,
                                     './/div[@class="input pr-6 pl-6 input_type_text input_size_default '
                                     'input_status_active"]']
    EYE = [By.XPATH, './/div[@class = "input__icon input__icon-action"]']

    @allure.step("Проверка текста в поле Восстановления пароля")
    def check_restore_password_text(self):
        actual_text = self.get_text(self.RESTORE_PASSWORD_TEXT)
        assert actual_text == 'Восстановление пароля'

    @allure.step("Ввод email")
    def entering_email(self):
        self.click(self.RESTORE_EMAIL_INPUT)
        self.send_input(self.RESTORE_EMAIL_INPUT, 'nf7q@yandex.ru')

    @allure.step("Клик на кнопку Восстановления пароля")
    def click_on_restore_button(self):
        self.click(self.RESTORE_BUTTON)
        self.wait_until_invisibility_element(self.RESTORE_BUTTON)

    @allure.step("Проверка текста в поле для получения кода из письма")
    def check_input_code_text_for_restore(self):
        actual_text = self.get_text(self.CODE_INPUT)
        assert actual_text == 'Введите код из письма'

    @allure.step("Клик на показать/скрыть пароль")
    def click_eye(self):
        self.click(self.EYE)

    @allure.step("Проверка активности поля для ввода пароля")
    def check_active_password_input(self):
        element = self.find_element(self.RESTORE_PASSWORD_ACTIVE_INPUT)
        assert element.is_displayed()
