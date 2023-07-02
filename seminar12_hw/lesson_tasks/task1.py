# Задание № 1
#
# - Создайте класс-функцию, который считает факториал числа при вызове экземпляра
# - Экземпляр должен запоминать последние k значений
# - Параметр k передаётся при создании экземпляра
# - Добавьте метод для просмотра ранее вызываемых значений и их факториалов

class Factorial:
    def __init__(self, k):
        self.k = k
        self.values = {}

    def calculate(self, number):
        if number in self.values:
            return self.values[number]

        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        self.values[number] = factorial

        # Если есть лишние значения в словаре уберём их из словаря
        if len(self.values) > self.k:
            self.values.pop(list(self.values.keys())[0])

        return factorial

    def get_values(self):
        return self.values


if __name__=='__main__':
    factorial = Factorial(3)
    for i in range(10):
        factorial.calculate(i)
    print(factorial.get_values())