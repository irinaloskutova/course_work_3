from coverage import data

import utils
from utils import *
import json


def main():
    data = utils.load_data('operations.json') #загрузили данные из файла 'operations.json'
    all_executed = get_executed_transaction(data) #получили список выполненных транзакций EXECUTED
    last_five_transactions = get_last_values(all_executed, 5) #получили список последних 5 транзакций
    for i in last_five_transactions:
        date = get_beautiful_date(i["date"]) #получили дату операции из транзакции
        operation = i["description"] #получили название операции из транзакции
        card_from = hide_part_number_from(last_five_transactions) #получили номер карты отправителя из транзакции
        card_to = hide_part_number_to(last_five_transactions) #получили номер карты получателя из транзакции
        print(date, operation)
        print(f'{card_from} -> {card_to}')
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    main()

