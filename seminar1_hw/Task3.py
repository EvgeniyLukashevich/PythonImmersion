# Task 3
# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print(f"Загадано число от {LOWER_LIMIT} до {UPPER_LIMIT}")
print("У вас есть 10 попыток, чтобы угадать это число. Удачи ;)")

for i in range(10):
    bingo_try = int(input(f"Попытка №{i+1}: "))

    if bingo_try == num:
        print(f"Поздравляю! Вы угадали число {num} за {i + 1} попыток!")
        break

    elif bingo_try < num:
        print("Загаданное число больше")

    else:
        print("Загаданное число меньше")

else:
    print("К сожалению вам не повезло")
    print(f"Было загадано число {num}")
