from .animal import Animal

__all__ = ['Eagle']


class Eagle(Animal):
    __TYPE = "Eagle"

    def __init__(self, name: str = "Зоркий Глаз", stamina: int = 15, flying_height: int = 2, stamina_consumption=1.5):
        super().__init__(name, stamina, stamina_consumption)
        self._flying_height = flying_height

    def get_flying_height(self):
        return self._flying_height

    def travelling(self, distance: int = 1, animal_type: str = __TYPE):
        super().travelling(distance, animal_type)

    def to_string(self):
        return super().to_string() + f"Вид животного: {self.__TYPE}\nВысота полета: {self._flying_height} км\n"

    def fly(self):
        print(f"{self.__TYPE} {self._name} поднялся на высоту {self._flying_height} км\n")
