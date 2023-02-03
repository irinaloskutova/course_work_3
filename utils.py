import datetime
import json

def load_data(filename):
    """загружаем данные из джейсон файла в формате списка словарей"""
    with open(filename, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data

def get_beautiful_date(data, a="%Y-%m-%dT%H:%M:%S.%f"):
        '''возвращает дату транзакции в "красивом" виде = день.месяц.год'''
        return datetime.datetime.strptime(data, a).strftime("%d.%m.%Y")


data = load_data('operations.json')
print(get_beautiful_date(data[0]['date']))
print(f"{data[0]['date']}")
print(f"{data[0]['description']} {data[0]['operationAmount']['currency']}")
print(f"{data[0]['from']} -> {data[0]['to']}")
print(f"{data[0]['operationAmount']['amount']} {data[0]['operationAmount']['currency']['name']}")