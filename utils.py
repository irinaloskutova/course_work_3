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
def get_one_transaction(data):
    '''перебирает по списку транзакций'''
    data_list = []
    for transaction in data:
        if transaction['state'] == 'EXECUTED':
            data_list.append(transaction)
    return data_list

def get_sorted(data):
    pass


def hide_part_number_from(data):
    """скрывает цифры из номера счета отправителя"""
    hide_part = data[0]['from'] #берет значение из from
    hide_part_first_word = hide_part.split(' ')[0] #берет первое слово из значения from
    hide_part_second_word_1 = list(hide_part.split(' ')[-1])[0:6] #берет первые 6 знаков из второго слова из значения from
    hide_part_second_word_2 = list(hide_part.split(' ')[1])[-4:] #берет последние 4 знака из второго слова из значения from
    return f"{hide_part_first_word} {''.join(hide_part_second_word_1)}******{''.join(hide_part_second_word_2)}"


def hide_part_number_to(data):
    """скрывает цифры из номера сета получателя"""
    hide_part = data[0]['to']  # берет значение из to
    hide_part_first_word = hide_part.split(' ')[0]  # берет первое слово из значения to
    hide_part_second_word = list(hide_part.split(' ')[1])[-4:]  # берет последние 4 знака из второго слова из значения to
    return f"{hide_part_first_word} **{''.join(hide_part_second_word)}"


# print(get_beautiful_date(data[0]['date']))
# print(f"{data[0]['date']}")
# print(f"{data[0]['description']} {data[0]['operationAmount']['currency']}")
# print(f"{data[0]['from']} -> {data[0]['to']}")
# print(f"{data[0]['operationAmount']['amount']} {data[0]['operationAmount']['currency']['name']}")
#
# print(hide_part_number_from(data))
#
print(get_one_transaction(data))