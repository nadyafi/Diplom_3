import allure

from data import URL
from helpers import create_order_by_api


class TestOrderFeed:
    @allure.title("Отображение всплывающего окна с деталями при клике на заказ")
    def test_order_details(self, main_page, order_feed):
        main_page.open(URL.MAIN)
        main_page.click_on_order_feed()
        order_feed.click_on_last_order()
        order_feed.check_details_popup()

    @allure.title("Заказы пользователя из раздела История заказов отображаются в Ленте заказов")
    def test_users_orders_in_order_feed(self, main_page, login_page, account_lk_page, create_order, order_feed):
        user_data = create_order[0]
        number = create_order[1]
        login_page.open(URL.LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        main_page.click_lk()
        account_lk_page.click_on_orders_history()
        main_page.click_on_order_feed()
        order_feed.check_order_number_in_list(number)

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increase_counter_all_time_orders(self, main_page, order_feed, register_new_user):
        main_page.open(URL.MAIN)
        user_data = register_new_user
        main_page.click_on_order_feed()
        counter_before = order_feed.get_number_of_orders_today()
        create_order_by_api(user_data)
        counter_after = order_feed.get_number_of_orders_today()

        assert counter_after > counter_before

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increase_counter_today_orders(self, register_new_user, main_page, order_feed):
        order_feed.open(URL.ORDER_FEED)
        user_data = register_new_user
        main_page.click_on_order_feed()
        counter_before = order_feed.get_number_of_orders_today()
        create_order_by_api(user_data)
        counter_after = order_feed.get_number_of_orders_today()

        assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, register_new_user, main_page, order_feed, login_page):
        user_data = register_new_user
        login_page.open(URL.LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        number = create_order_by_api(user_data)
        main_page.click_on_order_feed()

        assert order_feed.check_order_number_in_progress(number[2:]), f'Заказ в работе отсутствует'


