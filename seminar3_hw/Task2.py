# SEMINAR 3. HOMEWORK. TASK 2
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

# Установил пакет wikipedia, чтобы удобнее хранить текст статьи в переменной

import re
from pprint import pprint as pp
import wikipedia


def frequent_words(text: str) -> dict:
    # Уберем знаки препинания
    text = re.sub(r"[^\w\s]", '', text)
    # Переводим в нижний регистр
    text = text.lower()
    # Создаем список слов
    words = text.split()
    # Создаём словарь слов с упоминанием >9, где ключ - слово, значение - количество упоминаний
    new_dict = {word: words.count(word) for word in words if words.count(word) > 9}
    return new_dict


wikipedia.set_lang("ru")
page = wikipedia.page("Красно-черное дерево")
new_text = page.content

pp(frequent_words(new_text))
