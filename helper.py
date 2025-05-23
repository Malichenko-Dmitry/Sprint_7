import allure
import requests
import random
import string
from urls import URL


class CourierAPI:

    @allure.step('Создание курьера с заданными данными')
    def given_register_new_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        response = requests.post(URL.CREATE_COURIER, json=payload)
        if response.status_code == 201:
            return {'login': [login, password, first_name], 'response': response}
        else:
            return {'login': [login, password, first_name], 'response': response}


    @allure.step('Создание нового курьера')
    def create_courier(self, login=None, password=None, first_name=None):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(URL.CREATE_COURIER, data=payload)

        return {
            "login": payload["login"],
            "password": payload["password"],
            "first_name": payload["firstName"],
            "response": response
        }

    @allure.step('Авторизация созданного курьера')
    def login_courier(self, login, password):
        login_response = requests.post(URL.LOGIN_COURIER, data={'login': login, 'password': password})
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            return courier_id, login_response
        else:
            return None, login_response

    @allure.step('Удаление созданного курьера')
    def delete_courier(self, courier_id):
        url_delete = URL.DELETE_COURIER + str(courier_id)
        requests.delete(url_delete)

    @staticmethod
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))