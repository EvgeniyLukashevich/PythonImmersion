# Задание № 2
#
# - Создайте класс Архив, который хранит пару свойств. Например, число и строку
# - При создании нового экземпляра класса,
#   старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# - list-архивы также являются свойствами экземпляра

# Задание № 4
#
# - Доработаем класс Архив из задачи 2
# - Добавьте методы представления экземпляра для программиста и для пользователя


__all__ = ['Archive']


class Archive:
    """Класс Archive. Экземпляры класса хранят пару атрибутов число-строка.
    Сам же класс хранит списки чисел и строк всех созданных экземпляров класса"""
    numbers = []
    strings = []

    def __init__(self, number: int, string: str):
        """Инициализатор класса принимающий число и строку"""
        self._number = number
        self._string = string
        self.__class__.numbers.append(number)
        self.__class__.strings.append(string)

    def __str__(self):
        """Метод представления для пользователя"""
        text = f"Значения экземпляра: {self._number}, {self._string}\n"
        text += f"Архив чисел: {self.numbers}\nАрхив строк: {self.strings}\n"
        return text

    def __repr__(self):
        """Метод представления для программиста"""
        return f'Archive({self._number}, "{self._string}")'

    def get_numbers(self):
        """Метод возвращающий архив чисел"""
        return self.numbers

    def get_strings(self):
        """Метод, возвращающий архив строк"""
        return self.strings






