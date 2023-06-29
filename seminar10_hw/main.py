from homework_task1 import *
from homework_task2 import *

# Домашнее задание 1
factory = AnimalFactory()

animal = factory.create_animal('Animal', 'Зверь', stamina=5)
lion = factory.create_animal('Lion', 'Лёва', speed=55)
eagle = factory.create_animal('Eagle', 'Летун', flying_height=3)
shark = factory.create_animal('Shark', 'Улыбака', diving_depth=2)

print("\n\n# # # # # # # # # # # # # # # # # #\n\n")
print(lion.to_string())
lion.travelling(3)
print(lion.to_string())
lion.voice()
lion.eating(2)
print(lion.to_string())

print("\n\n# # # # # # # # # # # # # # # # # #\n\n")
print(animal.to_string())
animal.travelling(3)
print(animal.to_string())

print("\n\n# # # # # # # # # # # # # # # # # #\n\n")
print(eagle.to_string())
eagle.travelling(5)
print(eagle.to_string())
eagle.travelling(30)
print(eagle.to_string())
eagle.fly()

print("\n# # # # # # # # # # # # # # # # # #\n")
print(shark.to_string())
shark.travelling(2)
print(shark.to_string())
shark.dive()

# Домашнее задание 2
game = MysteryGame(tries_count=2)
game.start()
