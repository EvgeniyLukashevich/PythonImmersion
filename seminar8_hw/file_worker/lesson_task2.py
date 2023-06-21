# Задание № 2
#
# - Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# - После каждого ввода добавляйте новую информацию в JSON файл.
# - Пользователи группируются по уровню доступа.
# - Идентификатор пользователя выступает ключом для имени.
# - Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# - При перезапуске функции уже записанные в файл данные должны сохраняться.


import json
import os

__all__ = ['save_user_data_json']

_LEVELS_COUNT = 7


def save_user_data_json():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as user_file:
            users = json.load(user_file)
    else:
        users = {i: {} for i in range(1, _LEVELS_COUNT + 1)}

    while True:
        user_name = input("Введите Имя Пользователя (или 'q' для выхода): ")
        if user_name == 'q':
            print("Всего вам наилучшего :)")
            break

        user_id = input("Введите ID пользователя: ")
        if not user_id.isdigit():
            print('\nID Пользователя должно быть числом!')
            print("Давайте заново!\n")
            continue
        if not all(user_id not in user_data for user_data in users.values()):
            print("\nА АйДи то не уникален! ;)")
            print("Давайте заново!\n")
            continue

        user_level = input("Введите уровень доступа пользователя (от 1 до 7): ")
        if not user_level.isdigit():
            print('\nУровень доступа должен быть числом!')
            print("Давайте заново!\n")
            continue
        if int(user_level) < 1 or int(user_level) > 7:
            print("\nЧто-то вы как-то рассеяны.\nУровень доступа не должен быть меньше 1 и больше 7 ;)")
            print("Давайте заново!\n")
            continue

        users[user_level][user_id] = user_name

        with open('users.json', 'w') as user_file:
            json.dump(users, user_file)

        print("\nДАННЫЕ УСПЕШНО ЗАПИСАНЫ!\n")
