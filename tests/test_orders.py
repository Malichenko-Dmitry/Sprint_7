import allure
import pytest
import requests
from data import ORDERS
from urls import URL


class TestCreateOrder:
    @pytest.mark.parametrize(
        "order",
        [
            ORDERS.order_1,
            ORDERS.order_2,
            ORDERS.order_3,
            ORDERS.order_4,
        ]
    )

    @allure.title('Проверка успешного создания заказа')
    def test_create_order(self, order, create_order):
        assert create_order.status_code == 201
        content = create_order.json()
        assert "track" in content, "В ответе отсутствует поле 'track'"


class TestListOrders:

    @allure.title('Проверка успешного возврата заказа в теле ответа на запрос')
    def test_list_order(self):
        response = requests.get(URL.ORDER_LIST)
        assert response.status_code == 200
        content = response.json()
        assert "orders" in content