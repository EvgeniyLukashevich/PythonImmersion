from .lion import Lion
from .eagle import Eagle
from .shark import Shark
from .animal import Animal

__all__=['AnimalFactory']


class AnimalFactory:
    def create_animal(self, animal_type: str, name: str, **kwargs):
        if animal_type == "Lion":
            return Lion(name, **kwargs)
        elif animal_type == "Eagle":
            return Eagle(name, **kwargs)
        elif animal_type == "Shark":
            return Shark(name, **kwargs)
        elif animal_type == "Animal":
            return Animal(name, **kwargs)
        else:
            print("Несуществующий вид животного")
