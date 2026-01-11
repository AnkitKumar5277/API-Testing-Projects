import requests
import allure

base_url = "https://restful-booker.herokuapp.com"


# ---------- 1. AUTH ----------
@allure.title("Create Token")
def test_auth():
    url = base_url + "/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200

    token = response.json()["token"]
    assert type(token) == str
    return token


# ---------- 2. CREATE ----------
@allure.title("Create Booking")
def test_create():
    url = base_url + "/booking"
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

    response = requests.post(url, json=payload)
    assert response.status_code == 200

    booking_id = response.json()["bookingid"]
    assert booking_id is not None
    return booking_id


# ---------- 3. READ ----------
@allure.title("Read Booking")
def test_read():
    booking_id = test_create()
    url = base_url + f"/booking/{booking_id}"

    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Ankit"


# ---------- 4. UPDATE ----------
@allure.title("Update Booking")
def test_update():
    token = test_auth()
    booking_id = test_create()

    url = base_url + f"/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Pramod"


# ---------- 5. DELETE ----------
@allure.title("Delete Booking")
def test_delete():
    token = test_auth()
    booking_id = test_create()

    url = base_url + f"/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    response = requests.delete(url, headers=headers)
    assert response.status_code == 201
