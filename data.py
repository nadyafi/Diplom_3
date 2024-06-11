import requests
import json
import allure

import helpers


class URL:
    BASE = 'https://stellarburgers.nomoreparties.site/'
    MAIN = f'{BASE}'
    LOGIN_PAGE = f'{BASE}login'
    PROFILE_PAGE = f'{BASE}account/profile'
    RESTORE_PAGE = f'{BASE}forgot-password'
    RESET_PASSWORD_WITH_CODE_PAGE = f'{BASE}reset-password'
    ORDER_FEED = f'{BASE}feed'
    ORDER_HISTORY = f'{BASE}account/order-history'
    URL_API_REGISTER = f'{BASE}api/auth/register'
    URL_API_PLACE_ORDER = f'{BASE}api/orders'
    URL_API_USER = f'{BASE}api/auth/user'
    URL_API_LOGIN = f'{BASE}api/auth/login'


@allure.step("Cоздание заказа")
def create_order_by_api(user_data):
    payload = {
        "email": user_data.get("email"),
        "password": user_data.get("password")
    }
    response = requests.post(URL.URL_API_LOGIN, headers={"Content-type": "application/json"},
                             data=json.dumps(payload))
    token = response.json()["accessToken"]
    order = requests.post(URL.URL_API_PLACE_ORDER,
                          headers={"Content-type": "application/json", "Authorization": f'{token}'},
                          data=json.dumps(helpers.order_data))
    number = order.json()["order"]["number"]
    return f'#0{number}'
