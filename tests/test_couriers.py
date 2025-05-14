import allure
from data import COURIERS
from helper import CourierAPI


class TestCreationCourier:

    @allure.title('Проверка успешного создания рандомного курьера')
    def test_creating_courier_success(self, courier_data):
        courier_methods = CourierAPI()
        result = courier_methods.create_courier(**courier_data)
        assert result["response"].status_code == 201
        assert result["response"].json()["ok"] is True

    @allure.title('Проверка отсутствия возможности создать двух одинаковых курьеров')
    def test_creating_two_identical_courier(self, registered_courier):
        couriers_methods = CourierAPI()
        result = couriers_methods.given_register_new_courier(**COURIERS.courier_1)
        assert result['response'].status_code == 409
        content = result['response'].json()
        assert content.get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка создания курьера без логина и пароля')
    def test_register_new_courier_without_login_courier_2(self):
        couriers_methods = CourierAPI()
        courier = COURIERS.courier_2
        result = couriers_methods.given_register_new_courier(**courier)
        assert result['response'].status_code == 400
        content = result['response'].json()
        assert content.get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка создания курьера без логина и пароля')
    def test_register_new_courier_without_login_courier_3(self):
        couriers_methods = CourierAPI()
        courier = COURIERS.courier_3
        result = couriers_methods.given_register_new_courier(**courier)
        assert result['response'].status_code == 400
        content = result['response'].json()
        assert content.get("message") == "Недостаточно данных для создания учетной записи"


class TestLoginCourier:

    @allure.title('Проверка возможности авторизации курьером')
    def test_login_courier(self, registered_courier):
        couriers_methods = CourierAPI()
        courier_id, login_response = couriers_methods.login_courier(
            COURIERS.courier_1['login'],
            COURIERS.courier_1['password']
        )
        assert login_response.status_code == 200
        assert courier_id is not None

    @allure.title('Проверка возникновения ошибки при авторизации курьера с неверным логином')
    def test_login_courier_wrong_login(self, registered_courier):
        wrong_login = COURIERS.wrong_login_courier_1['login']
        correct_password = COURIERS.courier_1['password']
        couriers_methods = CourierAPI()
        courier_id, login_response = couriers_methods.login_courier(wrong_login, correct_password)
        assert login_response.status_code == 404
        content = login_response.json()
        assert content.get("message") == "Учетная запись не найдена"

    @allure.title('Проверка возникновения ошибки при авторизации курьера с неверным паролем')
    def test_login_courier_wrong_password(self, registered_courier):
        correct_login = COURIERS.courier_1['login']
        wrong_password = COURIERS.wrong_password_courier_1['password']
        couriers_methods = CourierAPI()
        courier_id, login_response = couriers_methods.login_courier(correct_login, wrong_password)
        assert login_response.status_code == 404
        content = login_response.json()
        assert content.get("message") == "Учетная запись не найдена"

    @allure.title('Проверка возникновения ошибки при авторизации курьера без логина')
    def test_login_courier_without_login(self, registered_courier):
        couriers_methods = CourierAPI()
        login = COURIERS.without_login_courier_1['login']
        password = COURIERS.courier_1['password']
        courier_id, login_response = couriers_methods.login_courier(login, password)
        assert login_response.status_code == 400
        content = login_response.json()
        assert content.get("message") == "Недостаточно данных для входа"

    @allure.title('Проверка возникновения ошибки при авторизации курьера без пароля')
    def test_login_courier_without_password(self, registered_courier):
        couriers_methods = CourierAPI()
        login = COURIERS.courier_1['login']
        password = COURIERS.without_password_courier_1['password']
        courier_id, login_response = couriers_methods.login_courier(login, password)
        assert login_response.status_code == 400
        content = login_response.json()
        assert content.get("message") == "Недостаточно данных для входа"

    @allure.title('Проверка возникновения ошибки при авторизации несуществующего курьера')
    def test_login_not_creating_courier(self):
        couriers_methods = CourierAPI()
        courier_id, login_response = couriers_methods.login_courier(COURIERS.courier_1['login'], COURIERS.courier_1['password'])
        assert login_response.status_code == 404
        content = login_response.json()
        assert content.get("message") == "Учетная запись не найдена"