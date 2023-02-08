import datetime
import json

import utils


def load_data(filename):
    """загружаем данные из джейсон файла в формате списка словарей"""
    with open(filename, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


def get_beautiful_date(data, a="%Y-%m-%dT%H:%M:%S.%f"):
    '''возвращает дату транзакции в "красивом" виде = день.месяц.год'''
    return datetime.datetime.strptime(data, a).strftime("%d.%m.%Y")


data = utils.load_data('operations.json')

def get_executed_transaction(data):
    '''Перебирает по списку транзакций и оставляет только те, у которых
    есть значение 'from',
    а значение ['state'] == 'EXECUTED'''
    data_list = []
    for transaction in data:
        if 'from' not in transaction:
            continue
        elif 'state' not in transaction:
            continue
        elif transaction['state'] == 'EXECUTED':
            data_list.append(transaction)
    return data_list


# def get_sorted(data):
#     data_list = []
#     i = 0
#     for transaction in data:
#         if data[i]['state'] == 'EXECUTED':
#             data_list.append(transaction)
#         i += 1
#         return data_list


def hide_part_number_from(data):
    """скрывает цифры из номера счета отправителя"""
    hide_part = data[0]['from']  # берет значение из from
    part_first_word = hide_part.split(' ')[0]  # берет 1 слово из значения from
    part_second_word = hide_part.split(' ')[1] # берет 2 слово из значения from
    if part_second_word.isalpha():
        part_first_word = f'{part_first_word} {part_second_word}'
        part_second_word1 = list(hide_part.split(' ')[-1])[0:4]  # берет первые 4 знака из 3 слова из значения from
        part_second_word2 = list(hide_part.split(' ')[-1])[4:6]  # берет вторые 2 знака из 3 слова из значения from
        part_second_word3 = list(hide_part.split(' ')[-1])[-4:]  # берет последние 4 знака из 3 слова из значения from
    elif part_second_word.isdigit():
        part_second_word1 = list(hide_part.split(' ')[1])[0:4]  # берет первые 4 знака из 3 слова из значения from
        part_second_word2 = list(hide_part.split(' ')[1])[4:6]  # берет вторые 2 знака из 3 слова из значения from
        part_second_word3 = list(hide_part.split(' ')[1])[-4:]  # берет последние 4 знака из 3 слова из значения from
    return f"{part_first_word} {''.join(part_second_word1)} {''.join(part_second_word2)}** **** {''.join(part_second_word3)}"


def hide_part_number_to(data):
    """скрывает цифры из номера сета получателя"""
    hide_part = data[0]['to']  # берет значение из to
    hide_part_first_word = hide_part.split(' ')[0]  # берет первое слово из значения to
    hide_part_second_word = list(hide_part.split(' ')[1])[
                            -4:]  # берет последние 4 знака из второго слова из значения to
    return f"{hide_part_first_word} **{''.join(hide_part_second_word)}"


# print(get_beautiful_date(data[0]['date']))
# print(f"{data[0]['date']}")
# print(f"{data[0]['description']} {data[0]['operationAmount']['currency']}")
# print(f"{data[0]['from']} -> {data[0]['to']}")
# print(f"{data[0]['operationAmount']['amount']} {data[0]['operationAmount']['currency']['name']}")
#
print(hide_part_number_from(data))
# print(data)
# print(get_executed_transaction(data))
# print(get_sorted(data))
