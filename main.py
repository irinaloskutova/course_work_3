from coverage import data

import utils
from utils import *
import json


# print(len(date))
# print(date[0]["id"])


def main():
    data = utils.load_data('operations.json')
    all_executed = get_executed_transaction(data)
    last_five_transactions = get_last_values(all_executed, 5)
    for i in last_five_transactions:
        date = get_beautiful_date(i["date"])
        operation = i["description"]
        card_from = hide_part_number_from(last_five_transactions)
        card_to = hide_part_number_to(last_five_transactions)
        print(date, operation)
        print(f'{card_from} -> {card_to}')
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    main()

