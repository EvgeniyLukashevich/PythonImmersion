# Задание
#
# - Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
#   Результаты обхода сохраните в файлы json, csv и pickle.
#     - Для дочерних объектов указывайте родительскую директорию.
#     - Для каждого объекта укажите файл это или директория.
#     - Для файлов сохраните его размер в байтах,
#       а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle

__all__ = ['save_directory_info']


def get_directory_size(directory: str) -> int:
    size = 0

    for dir_path, dir_names, file_names in os.walk(directory):
        for filename in file_names:
            file_path = os.path.join(dir_path, filename)
            size += os.path.getsize(file_path)

    return size


def get_directory_info(directory: str) -> list:
    info = []

    for dir_path, dir_names, file_names in os.walk(directory):
        for dir_name in dir_names:
            sub_dir_path = os.path.join(dir_path, dir_name)
            size = get_directory_size(sub_dir_path)
            info.append({"name": dir_name, "path": sub_dir_path, "type": "directory", "size": size})

        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            size = os.path.getsize(file_path)
            info.append({"name": file_name, "path": file_path, "type": "file", "size": size})

    return info


def save_directory_info(directory: str) -> None:
    with open("directory_info.json", "w", encoding='utf-8') as f:
        json.dump(get_directory_info(directory), f, indent=4)

    with open("directory_info.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "path", "type", "size"])
        for item in get_directory_info(directory):
            writer.writerow([item["name"], item["path"], item["type"], item["size"]])

    with open("directory_info.pickle", "wb") as f:
        pickle.dump(get_directory_info(directory), f)
