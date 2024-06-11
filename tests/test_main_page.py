import allure
from data import URL


class TestMainPage:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, main_page, login_page):
        login_page.open(URL.LOGIN_PAGE)
        main_page.click_on_constructor()
        main_page.assert_current_url(URL.MAIN)

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, main_page):
        main_page.open(URL.MAIN)
        main_page.click_on_order_feed()
        main_page.assert_current_url(URL.ORDER_FEED)

    @allure.title("Отображение всплывающего окна с деталями при клике на ингредиент")
    def test_details_popup(self, main_page):
        main_page.open(URL.MAIN)
        main_page.click_on_ingredient()
        main_page.check_details()

    @allure.title("Закрытие высплывающего окна с деталями по клику на крестик")
    def test_close_details_popup(self, main_page):
        main_page.open(URL.MAIN)
        main_page.click_on_ingredient()
        main_page.click_on_close_button()
        main_page.check_close_details_popup()

    @allure.title("Создание заказа")
    def test_create_order(self, main_page, login_page, register_new_user):
        user_data = register_new_user
        login_page.open(URL.LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        main_page.make_order()
        main_page.check_my_order()

    @allure.title("Увеличение счетчика ингредиента, при добавлении его в заказ")
    def test_ingredient_counter_up(self, main_page, login_page, register_new_user):
        user_data = register_new_user
        login_page.open(URL.LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        counter_before = main_page.get_ingredient_counter()
        main_page.make_order()
        counter_after = main_page.get_ingredient_counter()
        assert counter_after > counter_before
