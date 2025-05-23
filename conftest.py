import allure
import pytest
import requests
from urls import URL
from helper import CourierAPI
from data import COURIERS


@allure.step('Создание заказа')
@pytest.fixture()
def create_order(order):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(URL.CREATE_ORDER, json=order, headers=headers)
    return response

@allure.step('Создание курьера с рандомными данными')
@pytest.fixture
def courier_data():
    courier_methods = CourierAPI()
    login = f"test_user_{courier_methods.generate_random_string(5)}"
    password = courier_methods.generate_random_string(8)
    first_name = "TestUser"

    yield {
        "login": login,
        "password": password,
        "first_name": first_name
    }
    courier_id, _ = courier_methods.login_courier(login, password)
    courier_methods.delete_courier(courier_id)


@allure.step('Создание курьера с задананными данными и его удаление')
@pytest.fixture
def registered_courier():
    couriers_methods = CourierAPI()
    couriers_methods.given_register_new_courier(**COURIERS.courier_1)
    yield
    courier_id = couriers_methods.login_courier(
        COURIERS.courier_1['login'],
        COURIERS.courier_1['password']
    )
    if courier_id and courier_id[0]:
        couriers_methods.delete_courier(courier_id[0])