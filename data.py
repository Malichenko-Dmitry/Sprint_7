from faker import Faker

fake = Faker(locale="ru_RU")

class COURIERS:

    courier_1 = {
        "login": "Ninja",
        "password": "1234",
        "first_name": "Saske"
    }

    courier_2 = {
        "login": "",
        "password": "1234",
        "first_name": "Ivanov"
    }

    courier_3 = {
        "login": "Boris",
        "password": "",
        "first_name": "Britva"
    }

    wrong_password_courier_1 = {
        "password": "4321"
    }

    without_password_courier_1 = {
        "password": ""
    }

    wrong_login_courier_1 = {
        "login": "Minja",
    }

    without_login_courier_1 = {
        "login": "",
    }


class ORDERS:
    order_1 = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=5),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=5),
        "deliveryDate": fake.date_between(start_date='+1d', end_date='+30d').isoformat(),
        "comment": fake.sentence(),
        "color": ["BLACK"]
    }

    order_2 = order_1.copy()
    order_2["color"] = ["GREY"]

    order_3 = order_1.copy()
    order_3["color"] = ["GREY", "BLACK"]

    order_4 = order_1.copy()
    order_4["color"] = []

