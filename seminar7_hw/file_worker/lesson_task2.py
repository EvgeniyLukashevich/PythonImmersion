# Задание № 2
#
# - Напишите функцию, которая генерирует псевдоимена.
# - Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# - Полученные имена сохраните в файл.

from random import randint as ri
from random import choice as rch

__all__ = ['names_write']

_VOWELS = 'уеыаоэяию'
_CONSONANTS = 'йцкнгшщзхфвпрлджчсмтб'
_NAME_LENGTH_MIN = 4
_NAME_LENGTH_MAX = 7


def name_generate() -> str:
    name = str()
    name_length = ri(_NAME_LENGTH_MIN, _NAME_LENGTH_MAX)
    vowels_count = 0

    for i in range(name_length):
        letter = rch(rch([_VOWELS, _CONSONANTS]))

        if letter in _VOWELS:
            vowels_count += 1
        if i == 0:
            name += letter.capitalize()
        else:
            name += letter

    if vowels_count == 0:
        for _ in range(ri(1, name_length // 2)):
            letter_position = ri(1, name_length)
            name = name[:letter_position] + rch(_VOWELS) + name[letter_position + 1:]

    return name


# Попытался чуть более по-пайтоновски
def name_generate1() -> str:
    name_length = ri(_NAME_LENGTH_MIN, _NAME_LENGTH_MAX)
    letters = [rch(rch([_VOWELS, _CONSONANTS])) for _ in range(name_length)]
    vowels_count = sum([1 for letter in letters if letter in _VOWELS])
    name = ''.join([letters[0].capitalize() if i == 0 else letter for i, letter in enumerate(letters)])

    if vowels_count == 0:
        name = ''.join([name[:letter_position] + rch(_VOWELS) + name[letter_position + 1:]
                        if name[letter_position] not in _VOWELS
                        else name for letter_position in [ri(1, name_length)
                                                          for _ in range(ri(1, name_length // 2))]])

    return name


def names_write(names_count: int):
    with open('lesson_task2', 'a', encoding='utf-8') as file:
        for _ in range(names_count):
            print(name_generate1(), file=file)

