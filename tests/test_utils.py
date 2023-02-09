import pytest


from utils import *
@pytest.fixture
def tests_data():
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "send",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]
    return data

# def test_load_data('test_utils.tests_data'):
#     assert len(load_data('test_utils.tests_data')) == 100
    # assert load_data('operations.json') == os.Path

def test_get_beautiful_date(tests_data):
    assert get_beautiful_date(tests_data[0]['date']) == '26.08.2019'

def test_get_executed_transaction(tests_data):
    assert len(get_executed_transaction(tests_data)) == 2

def test_get_last_values(tests_data):
    assert len(get_last_values(tests_data, 2)) == 2

def test_hide_part_number_from(tests_data):
    assert hide_part_number_from(tests_data) == 'Maestro 1596 83** **** 5199'

def test_hide_part_number_to(tests_data):
    assert hide_part_number_to(tests_data) == 'Счет **9589'