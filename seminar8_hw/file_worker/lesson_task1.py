# Задание № 1
#
# - Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# - Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# - Имена пишите с большой буквы.
# - Каждую пару сохраняйте с новой строки.


import json
from pathlib import Path

__all__ = ['seminar6_file_to_json']


def seminar6_file_to_json(origin_file_name: str | Path, result_file_name: str | Path):
    with (
        open(origin_file_name, 'r', encoding='utf-8') as f_read,
        open(result_file_name, 'w', encoding='utf-8') as f_write
    ):
        data = f_read.read().split('\n')

        results = []

        for line in data:
            if line:
                name, number = line.split(': ')
                results.append({"name": name.title(), "number": float(number)})

        f_write.write(json.dumps(results, ensure_ascii=False))



