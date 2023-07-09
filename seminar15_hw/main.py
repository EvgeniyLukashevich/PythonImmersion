import logging
import argparse
from datetime import datetime as dt
from homework import *

time = dt.now().strftime("%Y-%m-%d %H:%M:%S")

FORMAT = '{levelname}. Модуль {name}. Строка: {lineno}. Сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Прямоугольник")

parser.add_argument(
    '-a', metavar='длина прямоугольника', type=float, help="введите длину прямоугольника", default=1)
parser.add_argument(
    '-b', metavar='ширина прямоугольника', type=float, help="введите ширину прямоугольника", default=1)

try:
    args = parser.parse_args()
except:
    logger.error(f"Ошибка ввода аргумента ({time})")
    quit()

try:
    rectangle = Rectangle(args.a, args.b)
    logger.info(f"Прямоугольник успешно создан ({time})")
    print(rectangle)
except RectangleSideValueException as e:
    logger.error(f"Введен отрицательный аргумент ({time})")
