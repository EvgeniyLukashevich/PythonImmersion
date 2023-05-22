# TASK 5. Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import math


def square_equation(a, b, c):
    # вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    # решаем уравнение в зависимости от значения дискриминанта
    if discriminant == 0:
        # уравнение имеет один корень
        root = -b / (2 * a)
        return root
    elif discriminant > 0:
        # уравнение имеет два корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        # комплексные корни это жесть, конечно ))
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


# получаем коэффициенты уравнения от пользователя
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# решаем уравнение, и в зависимости от типа переменных с корнями уравнения выводим результат
roots = square_equation(a, b, c)
if isinstance(roots, complex):
    print(f"Корни уравнения: {roots.real:.3f} + {roots.imag:.3f}j и {roots.real:.3f} - {roots.imag:.3f}j")
elif isinstance(roots, tuple):
    print(f"Корни уравнения: {roots[0]:.3f} и {roots[1]:.3f}")
else:
    print(f"Корень уравнения: {roots:.3f}")
