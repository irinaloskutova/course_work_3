import pytest

from utils import load_data, get_beautiful_date, get_executed_transaction, get_last_values, hide_part_number_from, hide_part_number_to


@pytest.fixture
def test_data():
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

def test_load_data(test_data):
    assert len(load_data(test_data)) == 3
    assert load_data(test_data) == []

def test_get_beautiful_date(test_data):
    assert get_beautiful_date(test_data[0]['date']) == '26.08.2019'

def test_get_executed_transaction(test_data):
    assert len(get_executed_transaction(test_data)) == 2

def test_get_last_values(test_data):
    assert len(get_last_values(test_data, 2)) == 2

def test_hide_part_number_from(test_data):
    print(hide_part_number_from(test_data[0]['from']))

def test_hide_part_number_to(test_data):
    assert hide_part_number_to(test_data[0]['to']) == 'Счет **9589'