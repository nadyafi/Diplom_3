from selenium import webdriver
import pytest
import requests
import json
import allure

from data import URL
from pages.main_page import MainPage
from pages.restore_password_page import RestorePage
from pages.login_page import LoginPage
from pages.order_feed import OrderFeed
from pages.account_page import AccountPage
from helpers import generate_new_user_data, create_order_by_api


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def restore_page(driver):
    return RestorePage(driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def account_lk_page(driver):
    return AccountPage(driver)


@pytest.fixture(scope='function')
def order_feed(driver):
    return OrderFeed(driver)


@allure.step("Генерация и регистрация нового пользователя")
@pytest.fixture(scope='function')
def register_new_user():
    user_data = generate_new_user_data()
    response = requests.post(URL.URL_API_REGISTER, headers={"Content-type": "application/json"},
                             data=json.dumps(user_data))
    response_data = response.json()
    token = response_data["accessToken"]
    yield user_data
    requests.delete(URL.URL_API_USER, headers={"Authorization": f'{token}'})


@allure.step("Создание заказа авторизованным пользователем")
@pytest.fixture(scope='function')
def create_order(register_new_user):
    user_data = register_new_user
    number = create_order_by_api(user_data)

    return user_data, number
