# **Allure Report (in Python + PyTest)**

- install required commands :
   Install Allure Commandline  
i. Node JS – [https://nodejs.org/en/download/prebuilt-installer]  (https://nodejs.org/en/download/prebuilt-installer)  
ii. cmd → `node --version`  
iii. cmd → `npm -g i allure-commandline`   
            iwr -useb get.scoop.sh | iex scoop install allure

- in terminal –> pip install allure-pytest
- in terminal -> pytest main.py --alluredir=reports
- you will get reports folder in your project path
- then type -> allure serve reports

- it will give you url on terminal in pycharm
- click this url you can see report

example: 
```python
import pytest
import allure

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1 + 1 == 2

@pytest.mark.smoke
def test_method4():
    print("this is pytest")
    assert 1 + 1 == 0 + 2
```

