import requests
import pytest
import allure
from websockets.legacy.http import read_response

# 1 auth
base_url = "https://restful-booker.herokuapp.com"

@allure.title("AUTH")
@allure.description("auth require post, full_url, headers, payload")
def test_auth():
    base_path = "/auth"
    full_url = base_url + base_path
    print(full_url)
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(full_url, headers=headers, json=payload)
    print(response)
    token = response.json()["token"]
    print(token)

    assert response.status_code == 200
    assert type(token) == str
    assert len(token) > 0
    return token

# 2 create
@allure.title("CREATE")
@allure.description("create require post, full_url, payload")
def test_create():
    base_path = "/booking"
    full_url = base_url + base_path
    print(full_url)
    payload = {
        "firstname": "Ankit",
        "lastname": "Kumar",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-10",
            "checkout": "2026-01-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(full_url, json = payload)
    print(response)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print("The Booking Id " + str(bookingid) + " is created.")
    assert response.json()["bookingid"] is not None
    assert response.status_code == 200
    return booking_id

# 3 read
@allure.title("READ")
@allure.description("read requires get, full_url")
def test_read():
    booking_id = test_create()
    base_path = "/booking/" + str(booking_id)
    full_url = base_url + base_path
    print(full_url)
    response = requests.get(full_url)
    print(response)
    read = response.json()

    assert response.status_code == 200
    assert response.json()["firstname"] == "Ankit"
    print(response.json()["firstname"])

# 4 update
@allure.title("UPDATE")
@allure.description("update require put, full_url, headers, payload, token, booking_id")
@pytest.mark.regression
def test_update():
    token = test_auth()
    booking_id = test_create()
    base_path = "/booking/" + str(booking_id)
    full_url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + token
    }
    payload = {
        "firstname": "Optimus",
        "lastname": "Prime",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Energone"
    }
    response = requests.put(full_url, headers=headers, json=payload)
    print(response)
    assert response.status_code==200
    assert response.json()["firstname"] == "Optimus"
    assert response.json()["bookingdates"]["checkout"] == "2019-01-01"
    print(response.json()["lastname"])

# 5 patch
@allure.title("PARTIAL UPDATE")
@allure.description("partial update require patch, full_url, headers, payload, token, booking_id")
def test_patch():
    token = test_auth()
    booking_id = test_create()
    base_path = "/booking/" + str(booking_id)
    full_url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + token
    }
    payload = {
        "firstname": "Bumble",
        "lastname": "Bee",
    }
    response = requests.patch(full_url, json=payload, headers=headers)
    print(response)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Bumble"
    print(response.json()["lastname"])

# 6 delete
@allure.title("DELETE")
@allure.description("delete requres delete, full_url, headers, token, booking_id")
def test_delete():
    booking_id = test_create()
    token = test_auth()
    base_path = "/booking/" + str(booking_id)
    full_url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + token
    }
    response = requests.delete(full_url, headers=headers)
    print(response)
    assert response.status_code == 201
    assert response.elapsed.total_seconds()<3

# 7 READ AFTER DELETE
    read_response = requests.get(full_url)
    print(read_response.text)
    print(read_response.status_code == 404)
    assert read_response.text == "Not Found"

# sample tests
def test_sample():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    get_response = requests.get(url=url_get)
    assert get_response.status_code == 200
    print("positive")

@pytest.mark.skip(reason="Not working,Skip it")
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 405
    print("negative")

def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {} # or wrong body / json
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"

# pytest main.py --alluredir=reports
# allure serve reports








