# SEMINAR 4. HOMEWORK. TASK 3
# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# Исходное задание из семинара 2:
# https://github.com/EvgeniyLukashevich/PythonImmersion/blob/main/seminar2_hw/lesson_work/lesson_task6.py


def welcome_message(balance):
    print(f"Ваш баланс: {balance}")


def set_tax(balance):
    if balance >= RICH:
        return 0.1
    else:
        return 0


def deposit(balance, count_operations, operations_list):
    amount = int(input("Введите сумму для пополнения (кратно 50): "))
    print()
    operations_list.append(("пополнение", amount))

    if amount % 50 != 0:
        print("Я не знаю купюр меньше пятидесятирублёвых...")
        print()
        return balance, count_operations, operations_list

    balance += amount
    count_operations += 1

    if count_operations % 3 == 0:
        bonus = balance * 0.03
        operations_list.append(("бонус", bonus))
        balance += bonus

    return balance, count_operations, operations_list


def take_cash(balance, count_operations, operations_list):
    amount = int(input("Введите сумму для снятия (кратно 50): "))
    print()
    operations_list.append(("снятие", amount))

    if amount % 50 != 0:
        print("Я не знаю купюр меньше пятидесятирублёвых...\n Сумма должна быть кратна 50.")
        print()
        return balance, count_operations, operations_list

    if amount > balance:
        print("Недостаточно средств на балансе")
        print()
        return balance, count_operations, operations_list

    commission = amount * 0.015
    if commission < 30:
        commission = 30
    elif commission > 600:
        commission = 600

    balance -= amount + commission
    count_operations += 1

    if count_operations % 3 == 0:
        bonus = balance * 0.03
        operations_list.append(("бонус", bonus))
        balance += bonus

    return balance, count_operations, operations_list


RICH = 5000000
balance = 0
count_operations = 0
tax = 0
operations_list = []

while True:
    welcome_message(balance)
    tax = set_tax(balance)

    action = input("Выберите действие\n(Пополнить, снять или выйти): ")
    print()

    if action == "выйти":
        print("Думаешь, ты ушёл надолго?")
        break
    elif action == "пополнить":
        balance, count_operations, operations_list = deposit(balance, count_operations, operations_list)
    elif action == "снять":
        balance, count_operations, operations_list = take_cash(balance, count_operations, operations_list)
    else:
        print("Неверный ввод, попробуйте еще раз")
        print()
        continue

    balance -= balance * tax

print(operations_list)  # выводим список операций после выхода из основного цикла while
