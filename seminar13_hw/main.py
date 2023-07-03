from homework import *

while True:
    try:
        side1 = int(input("Введите сторону a: "))
        side2 = int(input("Введите сторону b: "))
    except ValueError as e:
        print(e)
        print("Некорректный тип данных. Попробуйте снова\n")
        continue
    else:
        try:
            # Здесь можно проверить как отрабатывает исключение на предмет отрицательных значений
            # для длины одной из сторон
            rectangle1 = Rectangle(side1, side2)
            print(rectangle1)
            break
        except RectangleSideValueException as e:
            print(e)
            print("Попробуйте снова\n")


print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # #\n")


# Здесь можно проверить как отработает исключение на предмет типа длины отличного от int
try:
    side1 = 5
    side2 = 3.5
    print(f"Попытаемся создать прямоугольник со сторонами {side1} и {side2}")
    rectangle1 = Rectangle(side1, side2)
except RectangleSideTypeException as e:
    print(e)
