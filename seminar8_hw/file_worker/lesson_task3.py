# Задание № 3
#
# - Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv

__all__ = ['json_to_csv']


def json_to_csv(json_file: str, csv_file: str):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    rows = []
    for key, values in data.items():
        for id, name in values.items():
            rows.append({'level': int(key), 'id': int(id), 'name': name})

    with open(csv_file, 'w', newline='') as csv_file:
        fieldnames = ['level', 'id', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)




