from general_pack import *

MENU = "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n" \
       "               ДЗ 1 - -----------> (./general_pack/lesson_task7.py)\n" \
       "               ДЗ 2 - введите 'h2' (./general_pack/queens.py)\n" \
       "               ДЗ 3 - введите 'h3' (./general_pack/queens.py)\n" \
       "  Семинар.Задание 1 - -----------> (./general_pack/lesson_task1.py)\n" \
       "  Семинар.Задание 2 - введите 's2' (./general_pack/guess_game.py)\n" \
       "  Семинар.Задание 3 - -----------> (./general_pack/lesson_task3.py)\n" \
       "Семинар.Задания 4-6 - введите 's4' (./general_pack/mystery_game.py)\n" \
       "  Семинар.Задание 7 - введите 's7' (./general_pack/lesson_task7.py)\n" \
       "  Семинар.Задание 8 - -----------> (./general_pack)\n" \
       "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"

while (True):
    print(MENU)

    match input("Введите символы, соответствующие заданию: "):

        case "h2":
            q, x, y = map(
                int,
                input("Введите через пробел\n(количествоФерзей размерПоляПоГоризонтали размерПоВертикали): ")
                .split(' ')
            )
            peaceful_queens_check(q, x, y)
            print('\nВот случайная расстановка ферзей:\n')
            print_field(x, y)

        case "h3":
            q, x, y, i, b = map(
                int,
                input(
                    "Введите через пробел\n(количествоФерзей "
                    "размерПоляПоГоризонтали размерПоВертикали "
                    "количествоИтераций количествоУспешныхКомбинаций): ")
                .split(' ')
            )
            peaceful_queens(q, x, y, i, b)

        case "s2":
            guess_number(10, 20, 5)

        case "s4":
            for tries in mysteries(3):
                print(f"Функция вернула: {tries}\n")

        case "s7":
            if is_valid_date(input("Введите дату для проверки: ")):
                print("Такая дата существует =)")
            else:
                print("Ну, может, в другой раз :(")

        case _:
            print("Всего доброго!")
            break
