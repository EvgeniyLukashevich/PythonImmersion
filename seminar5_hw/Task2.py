# SEMINAR 5. HOMEWORK. TASK 2
# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.


def bonus_dict_generator(names: list, salaries: list, bonuses: list) -> dict:
    """
    Метод с однострочным генератором словаря из трёх списком (имена, ставки, премии)
    :param names: словарь имён (str)
    :param salaries: словарь ставок (int)
    :param bonuses: словарь премий (str)
    :return: словарь с именем в качестве ключа и рассчитанной премией в качестве значения
    """
    return {name: salary * float(bonus.replace('%', '')) / 100 for name, salary, bonus in
            zip(names, salaries, bonuses)}


# Используя метод
bonus_dict = bonus_dict_generator(["Василий", "Петр", "Иван"], [10000, 20000, 30000], ["10.25%", "10.2%", "10.0%"])
print(bonus_dict)

# Без метода. Просто с генератором в одну строку
names_list = ["Николай", "Дмитрий", "Владимир"]
salaries_list = [50000, 100000, 150000]
bonuses_list = ["7.25%", "6.2%", "5.0%"]
new_dict = {name: salary * float(bonus.replace('%', '')) / 100 for name, salary, bonus in
            zip(names_list, salaries_list, bonuses_list)}
print(new_dict)
