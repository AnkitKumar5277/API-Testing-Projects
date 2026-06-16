import pytest
import requests
from dotenv import load_dotenv
import os

@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print("Creating Token....")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    response.raise_for_status()  # raises error if status != 200
    token = response.json().get("token")
    assert response.json()[username]=="admin"
    return token
# Creating Token....
# Token -> abc123xyz

@pytest.fixture()
def create_booking_id():
    print("Creating Booking ID....")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    response.raise_for_status()
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

@pytest.fixture()
def read_csv_file_data():
    # implement logic to read CSV later
    return []

@pytest.fixture()
def read_mysql_file_database():
    # implement logic to connect to MySQL later
    return None

@pytest.fixture()
def read_url_testdata_excel():
    # implement logic to read Excel test data later
    return None

@pytest.fixture()
def launch_browser():
    print("Launching Chrome browser...")
    yield "chrome"   # test runs here
    print("Closing Chrome browser...")  # teardown after test
