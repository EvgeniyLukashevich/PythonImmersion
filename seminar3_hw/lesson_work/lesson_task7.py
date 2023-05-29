# Пользователь вводит строку текста.
# Посчитайте сколько раз встречается каждая буква в строке
# без использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ,
# а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните, почему они совпадают или нет в ваших решениях.

from pprint import pprint as pp


def with_count(text: str) -> dict:
    uniq_chars = set(text)
    new_dict = {char: text.count(char) for char in uniq_chars}
    return new_dict


def without_count(text: str) -> dict:
    new_dict = {}

    for char in text:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    return new_dict


user_input = input('Введите строку: ')

pp(without_count(user_input))
pp(with_count(user_input))
