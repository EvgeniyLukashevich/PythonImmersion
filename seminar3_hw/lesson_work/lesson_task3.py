# Создайте вручную кортеж, содержащий элементы разных типов.
# Получите из него словарь списков, где:
#  * ключ - тип элемента
#  * значение - список элементов данного типа

from pprint import pprint as pp

origin_tuple = (
    "1st", 1, .1, ["1st", 1, .1], ("1st", 1, .1), {1: 1, 2: .1}, {1, .1, "first"}, True,
    "2nd", 2, .2, ["2nd", 2, .2], ("2nd", 2, .2), {1: 2, 2: .2}, {2, .2, "second"}, False,
    "3rd", 3, .3, ["3rd", 3, .3], ("3rd", 3, .3), {1: 3, 2: .3}, {3, .3, "third"}, True)


# короткое решение
def from_tuple_to_dict(inner_tuple: tuple) -> dict:
    new_dict = {}

    for item in inner_tuple:
        item_type = type(item).__name__
        if item_type not in new_dict:
            new_dict[item_type] = []
        new_dict[item_type].append(item)

    return new_dict


my_dict = from_tuple_to_dict(origin_tuple)
pp(my_dict)
