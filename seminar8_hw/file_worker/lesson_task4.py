# Задание № 4
#
# - Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# - Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# - Добавьте поле хеш на основе имени и идентификатора.
# - Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# - Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json
import hashlib

__all__ = ['csv_to_json']


def csv_to_json(csv_file: str, json_file: str):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            d = {header[0]: int(row[0]), header[1]: row[1].zfill(10), header[2]: row[2].capitalize(),
                 "hash": hashlib.md5((row[1] + row[2]).encode()).hexdigest()}
            data.append(d)
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)
