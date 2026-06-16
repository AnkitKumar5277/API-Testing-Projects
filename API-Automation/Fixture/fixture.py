import pytest
@pytest.fixture()
def is_married_before_run():
    return True

def test_update(is_married_before_run):
    assert is_married_before_run == True

#------------------------------------------

@pytest.fixture
def sample_data():
    print("\nFixture run ho raha hai")
    return {"name": "Ankit", "age": 25}

def test_example(sample_data):
    print("Test case run ho raha hai")
    assert sample_data["name"] == "Ankit"
# Pytest me fixture ek special function hota hai
# jo test case run hone se pehle ya baad me automatically execute hota ha
