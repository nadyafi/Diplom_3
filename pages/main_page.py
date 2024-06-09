from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    LK = [By.XPATH, ".//a[@href='/account']"]  # Личный кабинет в хедере
    CONSTRUCTOR = [By.XPATH, ".//a[contains(@class, 'AppHeader_header__link')][@href='/']"]  # Ссылка на Конструктор
    ORDER_FEED = [By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]
    BUN_INGREDIENT = [By.XPATH, "//a[1][contains(@class, 'BurgerIngredient_ingredient')]"]
    SAUCE_INGREDIENT = [By.XPATH, "//a[3][contains(@class, 'BurgerIngredient_ingredient')]"]
    TOPPING_INGREDIENT = [By.XPATH, "//a[7][contains(@class, 'BurgerIngredient_ingredient')]"]
    DETAILS = [By.XPATH, ".//h2[@class= 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m "
                         "text text_type_main-large pl-10']"]
    CLOSE = [By.XPATH, ".//button[1][@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    POPUP = [By.XPATH, ".//div[@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15']"]
    MY_BURGER = [By.XPATH, "//span[1][@class = 'constructor-element__row']"]
    ORDER_PLACED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"]
    INGREDIENT_COUNTER = [By.XPATH,
                          ".//a[contains(@class, 'BurgerIngredient_ingredient_')]//p[contains(@class, 'counter_counter__num')]"]

    @allure.step("Клик на Личный кабинет")
    def click_lk(self):
        self.click(self.LK)

    @allure.step("Клик на Конструктор")
    def click_on_constructor(self):
        self.click(self.CONSTRUCTOR)

    @allure.step("Клик на Лента заказов")
    def click_on_order_feed(self):
        self.click(self.ORDER_FEED)

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self):
        self.click(self.BUN_INGREDIENT)

    @allure.step("Клик на крестик закрытия")
    def click_on_close_button(self):
        self.click(self.CLOSE)

    @allure.step("Проверка деталей ингредиента")
    def check_details(self):
        for elements in [self.BUN_INGREDIENT, self.DETAILS, self.CLOSE]:
            find = self.find_element(elements)
            assert find.is_displayed()

    @allure.step("Проверка закрытия всплывающего окна с деталями")
    def check_close_details_popup(self):
        popup = self.find_element(self.POPUP)
        visibility = popup.get_attribute("visibility")
        assert visibility != "visible"

    @allure.step("Создание заказа")
    def make_order(self):
        bun = self.find_element(self.BUN_INGREDIENT)
        sauce = self.find_element(self.SAUCE_INGREDIENT)
        topping = self.find_element(self.TOPPING_INGREDIENT)
        my_burger = self.find_element(self.MY_BURGER)
        for i in [bun, sauce, topping]:
            self.drag_and_drop(i, my_burger)
        self.click(self.ORDER_BUTTON)

    @allure.step("Проверка оформления заказа")
    def check_my_order(self):
        if self.find_element(self.ORDER_PLACED):
            return True

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.get_text(self.INGREDIENT_COUNTER)
        return counter
