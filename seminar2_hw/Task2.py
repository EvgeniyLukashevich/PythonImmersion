# SEMINAR 2. HOMEWORK. TASK 2
# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и произведение дробей. Для проверки своего
# кода используйте модуль fractions

from fractions import Fraction


# ищем наибольший общий делитель
# принимаем в качестве аргументов два знаменателя
# функция рекурсивно вызывает саму себя с аргументами одного знаменателя и остатком от деления второго на первый
# поочередно, с каждым уровнем рекурсии, меняя местами аргументы
# выходим, когда один из знаменателей окажется равен нулю
def divider(den1: int, den2: int) -> int:
    if den2 == 0:
        return den1
    else:
        return divider(den2, den1 % den2)


# функция сложения двух дробей
# принимаем два числителя и два знаменателя
# и возвращаем кортежик из итоговых числителя и знаменателя
def fraction_sum(num1: int, den1: int, num2: int, den2: int) -> tuple:
    den = den1 * den2 // divider(den1, den2)
    num = num1 * (den // den1) + num2 * (den // den2)
    return (num, den)


# функция произведения двух дробей
# аргументы и возврат функции аналогичен функции сложения
def fraction_product(num1: int, den1: int, num2: int, den2: int) -> tuple:
    num = num1 * num2
    den = den1 * den2
    return (num, den)


# просим ввести дроби нужного нам формата
fraction1 = input("Введите первую дробь (a/b): ")
fraction2 = input("Введите вторую дробь (a/b): ")

# отделим числитель от знаменателя
num1, den1 = map(int, fraction1.split("/"))
num2, den2 = map(int, fraction2.split("/"))

# вычислим сумму и произведение дробей
sum_num, sum_den = fraction_sum(num1, den1, num2, den2)
prod_num, prod_den = fraction_product(num1, den1, num2, den2)

# выводим и проверяем, с помощью встроенного модуля
print(f"Сумма дробей: {sum_num}/{sum_den}. Проверка: {Fraction(fraction1) + Fraction(fraction2)}")
print(f"Произведение дробей: {prod_num}/{prod_den}. Проверка: {Fraction(fraction1) * Fraction(fraction2)}")
