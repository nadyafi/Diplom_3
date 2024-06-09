import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    EXIT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Account_button')][text()='Выход']"]
    # Кнопка Выход из Личного кабинета
    PROFILE_IN_LK = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"]  # Профиль в Личном кабинете
    ORDERS_HISTORY = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"]
    ORDER_HISTORY_INACTIVE = [By.XPATH, "//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
    ORDER_HISTORY_ACTIVE = [By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]

    @allure.step("Проверка, что открылась страница личного кабинета")
    def check_opened_account_page(self):
        element = self.find_element(self.PROFILE_IN_LK)
        assert element.is_displayed()

    @allure.step("Клик на История заказов")
    def click_on_orders_history(self):
        self.click(self.ORDERS_HISTORY)

    @allure.step("Клик Выход")
    def click_exit(self):
        self.click(self.EXIT_BUTTON)

    @allure.step('Проверка, что таб История заказов неактивен')
    def check_order_history_inactive(self):
        return self.find_element(self.ORDER_HISTORY_INACTIVE)

    @allure.step('Проверка, что таб История заказов активен')
    def check_order_history_active(self):
        return self.find_element(self.ORDER_HISTORY_ACTIVE)






