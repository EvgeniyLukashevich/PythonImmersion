# SEMINAR 3. HOMEWORK. TASK 1
# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов...

from random import randint as ri


def not_uniq_list(inner_list: list) -> list:
    new_set = {element for element in inner_list if inner_list.count(element) > 1}
    return list(new_set)


origin_list = [ri(1, 20) for _ in range(15)]

print("Исходный список:", origin_list, "\n")
print("Результат:", not_uniq_list(origin_list))
