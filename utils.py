import datetime
import json

import utils


def load_data(filename):
    """загружаем данные из джейсон файла в формате списка словарей"""
    with open(filename, 'r', encoding='UTF-8') as f:
        result = json.load(f)
        return result


def get_beautiful_date(data, a="%Y-%m-%dT%H:%M:%S.%f"):
    '''возвращает дату транзакции в "красивом" виде = день.месяц.год'''
    return datetime.datetime.strptime(data, a).strftime("%d.%m.%Y")

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

def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_last_values]

def hide_part_number_from(data):
    """скрывает цифры из номера счета отправителя"""
    for i in data:
        # hide_part = i['from']  # берет значение из from
        part_first_word = i['from'].split(' ')[0]  # берет 1 слово из значения from
        part_second_word = i['from'].split(' ')[1] # берет 2 слово из значения from
        if part_second_word.isalpha():
            part_first_word = f'{part_first_word} {part_second_word}'
            part_second_word1 = list(i['from'].split(' ')[-1])[0:4]  # берет первые 4 знака из 3 слова из значения from
            part_second_word2 = list(i['from'].split(' ')[-1])[4:6]  # берет вторые 2 знака из 3 слова из значения from
            part_second_word3 = list(i['from'].split(' ')[-1])[-4:]  # берет последние 4 знака из 3 слова из значения from
        elif part_second_word.isdigit():
            part_second_word1 = list(i['from'].split(' ')[1])[0:4]  # берет первые 4 знака из 3 слова из значения from
            part_second_word2 = list(i['from'].split(' ')[1])[4:6]  # берет вторые 2 знака из 3 слова из значения from
            part_second_word3 = list(i['from'].split(' ')[1])[-4:]  # берет последние 4 знака из 3 слова из значения from
        a = f"{part_first_word} {''.join(part_second_word1)} {''.join(part_second_word2)}** **** {''.join(part_second_word3)}"
        # print(a)
        return a

def hide_part_number_to(data):
    """скрывает цифры из номера сета получателя"""
    hide_part = data[0]['to']  # берет значение из to
    hide_part_first_word = hide_part.split(' ')[0]  # берет 1 слово из значения to
    hide_part_second_word = list(hide_part.split(' ')[1])[-4:]  # берет последние 4 знака из 2 слова из значения to
    return f"{hide_part_first_word} **{''.join(hide_part_second_word)}"



