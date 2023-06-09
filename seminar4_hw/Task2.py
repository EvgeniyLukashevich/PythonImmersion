# SEMINAR 4. HOMEWORK. TASK 2
# Напишите функцию, принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs) -> dict:
    """
    Создает словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
    :param kwargs: ключевые параметры
    :return: словарь с именами и значение переданных параметров.
    """
    result_dict = {}
    for key, value in kwargs.items():
        if not hash(key):
            key = str(key)
        result_dict[value] = key
    return result_dict

def create_dict2(**kwargs):
    """
    Создает словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
    Нехешируемые типы приводятся к строковому виду.
    Значения коллекций переводятся в строковый вид.
    :param kwargs: ключевые параметры
    :return: словарь с именами и значение переданных параметров.
    """
    result_dict = {}
    for key, value in kwargs.items():
        if not isinstance(key, (str, int, float, complex, bool)):
            key = str(key)
        if isinstance(value, (list, tuple, set, dict)):
            value = str(value)
        result_dict[value] = key
    return result_dict


new_dict = create_dict2(a=12, b=3.55, name="Evgeniy", list=[3, 7.55, "hi"])
print(new_dict)
