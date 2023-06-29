from .animal import Animal

__all__ = ['Lion']


class Lion(Animal):
    __TYPE = "Lion"
    __VOICE = "'Ррр'"

    def __init__(self, name: str = "Кис-кис-кис", stamina: int = 15, speed: int = 45, stamina_consumption=0.5):
        super().__init__(name, stamina, stamina_consumption)
        self._speed = speed

    def get_speed(self):
        return self._speed

    def travelling(self, distance: int = 1, animal_type: str = __TYPE):
        super().travelling(distance, animal_type)

    def to_string(self):
        return super().to_string() + f"Вид животного: {self.__TYPE}\nСкорость: {self._speed} км/ч\n"

    def voice(self):
        print(f"{self.__TYPE} {self._name} сказал(-а) {self.__VOICE}")
        print(f"А потом похвастался, что может бегать со скоростью {self._speed} км/ч\n")
