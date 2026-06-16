import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

def test_put(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)

def test_put_2(create_token, create_booking_id, read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)



import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests

# pytest main.py --alluredir=reports
# allure serve reports
import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 123

@pytest.fixture()
def read_csv_file_data():
    return "xyz"

def test_update_req_1(create_token):
    print("Booking ID -> ", create_booking_id)

def test_update_req_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

def test_update_req_3(create_token, create_booking_id, read_csv_file_data):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)
    print("Excel File ->", read_csv_file_data)
