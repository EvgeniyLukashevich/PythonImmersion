from .animal import Animal

__all__ = ['Shark']


class Shark(Animal):
    __TYPE = "Shark"

    def __init__(self, name: str = "Челюсть", stamina: int = 15, diving_depth: int | float = 1.5,
                 stamina_consumption=0.2):
        super().__init__(name, stamina, stamina_consumption)
        self._diving_depth = diving_depth

    def get_diving_depth(self):
        return self._diving_depth

    def travelling(self, distance: int = 1, animal_type: str = __TYPE):
        super().travelling(distance, animal_type)

    def to_string(self):
        return super().to_string() + f"Вид животного: {self.__TYPE}\nГлубина погружения: {self._diving_depth} км\n"

    def dive(self):
        print(f"{self.__TYPE} {self._name} погрузил(-ся/ась) на глубину {self._diving_depth} км\n")
