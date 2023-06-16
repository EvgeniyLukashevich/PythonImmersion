# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# SEMINAR 6. HOMEWORK. TASK 1
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

__all__ = ['is_valid_date']

def is_valid_date(date_str):
    day, month, year = date_str.split('.')

    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return False

    if year <1 or year >9999:
        return False

    if month < 1 or month >12:
        return False

    if month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if is_leap_year(year):
            max_day =29
        else:
            max_day =28
    else:
        max_day = 31

    if day < 1 or day > max_day:
        return False

    return True


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    # Принимаем аргумент через терминал
    if len(argv) > 1:
        if is_valid_date(argv[1]):
            print("Дата существует :)")
        else:
            print("Неа, нет такой даты")
    else:
        print("Введите дату в формате DD.MM.YYYY")

