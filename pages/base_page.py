import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Открытие страницы')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Ожидание элемента и ввод данных')
    def send_input(self, locator, data):
        return self.driver.find_element(*locator).send_keys(data)

    @allure.step('Сравнение текущего URL с ожидаемым')
    def assert_current_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'{actual_url} != {expected_url}'

    @allure.step('Получение текста из элемента')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Перетаскивание элементов')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(3).perform()

    @allure.step("Ожидание, пока элемент пропадет со страницы")
    def wait_until_invisibility_element(self, locator):
        WebDriverWait(self.driver, 25).until(ec.invisibility_of_element_located(locator))

    @staticmethod
    def concat_locator_and_number(locator, value):
        method, locator = locator
        return method, locator.format(value)
