import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderFeed(BasePage):
    ORDER = [By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6'][1]"]
    NUMBER_ORDER_FROM_FEED = [By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    CONTAIN = [By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']"]
    CONTAINING_ELEMENTS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default'][1]"]
    STATUS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default mb-15']"]
    ORDER_IN_ORDER_FEED = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    COMPLETED_ORDERS_TODAY_BEFORE = [By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p"]
    LABEL_ALL_ORDERS_ARE_READY = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"
                                            "/li[text()='Все текущие заказы готовы!']"]
    ORDER_LIST = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"]

    @allure.step("Клик на последний заказ")
    def click_on_last_order(self):
        self.click(self.ORDER)

    @allure.step("Проверка всплвающего окна с деталями заказа")
    def check_details_popup(self):
        for elements in [self.NUMBER_ORDER_FROM_FEED, self.CONTAIN, self.CONTAINING_ELEMENTS, self.STATUS]:
            find = self.find_element(elements)
            assert find.is_displayed()

    @allure.step("Проверка, что номер заказа есть в Истории заказов и в Ленте заказов")
    def check_order_number_in_list(self, number):
        history_text = self.get_order_number_in_feed()
        feed_text = self.get_order_number_in_feed()
        for i in [history_text, feed_text]:
            if number in i:
                return True
            else:
                return False

    @allure.step("Проверка, что номер заказа есть в разделе В работе")
    def check_order_number_in_progress(self, number):
        self.wait_until_invisibility_element(self.LABEL_ALL_ORDERS_ARE_READY)
        order_locator = self.concat_locator_and_number(self.ORDER_LIST, number)
        if self.find_element(order_locator):
            return True
        else:
            return False

    @allure.step('Получение номера последнего заказа в ленте')
    def get_order_number_in_feed(self):
        element = self.find_element(self.ORDER_IN_ORDER_FEED)
        return element.text

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_number_of_orders_today(self):
        number = self.get_text(self.COMPLETED_ORDERS_TODAY_BEFORE)
        return number
