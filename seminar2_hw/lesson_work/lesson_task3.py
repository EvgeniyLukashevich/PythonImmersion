# SEMINAR 2. TASK 3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


# Сделаю через функцию, чтобы не было привязки к конкретным системам счисления
def number_convert(num: int, base: int) -> str:
    # символы, достаточные для вычисления шестнадцатеричного числа
    # можно было все прописать, чтобы охватить побольше систем
    digits = "0123456789ABCDEF"
    result = ""
    while num > 0:
        digit = num % base
        result += digits[digit]
        num //= base
    # возвращаем строку в обратном порядке
    return result[::-1]


# получаем число от пользователя
num = int(input("Введите целое число: "))

# преобразуем в двоичную систему счисления
binary = number_convert(num, 2)
print(f"Двоичное представление: {binary} (проверка: {bin(num)})")

# преобразуем в восьмеричную систему счисления
octal = number_convert(num, 8)
print(f"Восьмеричное представление: {octal} (проверка: {oct(num)})")