__all__ = ['Animal']


class Animal:
    __KINGDOM = "Animal"

    def __init__(self, name: str = 'Неизвестное Животное', stamina: int = 10, stamina_consumption: int | float = 1):
        self._name = name
        self._stamina = stamina
        self._stamina_consumption = stamina_consumption

    def get_kingdom(self):
        return self.__KINGDOM

    def get_name(self):
        return self._name

    def get_stamina(self):
        return self._stamina

    def eating(self, food_amount: int = 1):
        print(f"{self._name} перекусил(-a)\n")
        self._stamina += food_amount

    def travelling(self, distance: int = 1, animal_type: str = __KINGDOM):
        if self._stamina <= 0:
            print(f"{animal_type} {self._name} необходимо перекусить\n")
            return False
        elif self._stamina - distance * self._stamina_consumption < 0:
            print(f"{animal_type} {self._name} не сможет пройти этот путь\n")
            return False
        else:
            self._stamina -= round(distance * self._stamina_consumption, 2)
            print(f"{animal_type} {self._name} куда-то передвигается на {distance} км\n")
            return True

    def to_string(self):
        return f"Имя: {self._name}\nЦарство: {self.__KINGDOM}\nВыносливость: {self._stamina}\n"
