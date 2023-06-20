from random import randint as ri
from file_worker import *

# Задание № 1 с семинара
# int_float_writer("lesson_task1", ri(5, 7))

# Задание № 2 с семинара
# names_write(ri(2, 4))

# Задание № 3 с семинара
# from_f1_and_f2_to_f3('lesson_task1','lesson_task2')

# Задание № 4 с семинара
# create_files('', num_files=2)

# Задание № 5 с семинара
# create_files2({'txt': 2, 'png': 3}, min_name_length=2, max_name_length=12, min_size=128, max_size=512)

# Задание № 6 с семинара
# create_files3(
#     {'txt': 2, 'png': 3}, 'lesson_task6_dir', min_name_length=4, max_name_length=8, min_size=64, max_size=256
# )

# Домашнее задание № 1
rename_files('hw_task1_dir', '_hw_task1_', 3, '.txt', '.md', [2, 4])
