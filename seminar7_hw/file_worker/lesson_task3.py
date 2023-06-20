# Задание № 3
#
# - Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# - Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#     - если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
#     - если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
#     - В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# - При достижении конца более короткого файла, возвращайтесь в его начало.


from pathlib import Path

__all__ = ['from_f1_and_f2_to_f3']


def from_f1_and_f2_to_f3(first_file_name: str | Path, second_file_name: str | Path) -> None:
    with (
        open(first_file_name, 'r', encoding='utf-8') as file1,
        open(second_file_name, 'r', encoding='utf-8') as file2,
        open('lesson_task3', 'w', encoding='utf-8') as result_file
    ):
        f1_lines = file1.readlines()
        f2_lines = file2.readlines()

        for i in range(max(len(f1_lines), len(f2_lines))):
            num1, num2 = map(float, f1_lines[i % len(f1_lines)].strip().split('|'))
            name = f2_lines[i % len(f2_lines)].strip()
            product = num1 * num2

            if product < 0:
                name = name.lower()
                product = abs(product)
            else:
                name = name.upper()
                product = round(product)

            print(f'{name}: {product}', file=result_file)


