import requests
import pytest
import allure

base_url = "https://restful-booker.herokuapp.com"


# ---------- AUTH ----------
@pytest.fixture()
def auth_token():
    url = base_url + "/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    return response.json()["token"]


# ---------- CREATE ----------
@pytest.fixture()
def create_booking():
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
    return response.json()["bookingid"]


# ---------- READ ----------
@allure.title("Read Booking")
def test_read_booking(create_booking):
    url = base_url + f"/booking/{create_booking}"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Ankit"


# ---------- UPDATE ----------
@allure.title("Update Booking")
def test_update_booking(create_booking, auth_token):
    url = base_url + f"/booking/{create_booking}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
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


# ---------- DELETE ----------
@allure.title("Delete Booking")
def test_delete_booking(create_booking, auth_token):
    url = base_url + f"/booking/{create_booking}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }

    response = requests.delete(url, headers=headers)
    assert response.status_code == 201
