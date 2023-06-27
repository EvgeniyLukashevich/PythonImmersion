__all__ = ['mystery', 'mysteries']

_result_dict = dict()


def mystery(question: str, answers: list, tries_count: int) -> int:
    current_try = 0
    print(f"Загадка. {question}")

    while current_try < tries_count:

        if input("Твой вариант ответа: ") in answers:
            current_try += 1
            myst_tries(question, current_try)
            print(f"Верно! Тебе понадобилось попыток: {current_try}\n")
            return current_try

        else:
            current_try += 1
            print(f"\nНеверно! Попыток осталось: {tries_count - current_try}")

    print(f"К сожалению попытки закончились! Верный ответ: {answers[0]}\n")
    myst_tries(question, tries_count - current_try)
    return tries_count - current_try


# Хотелось бы словарь хранить в модуле, а не в функции, но по условию задачи надо именно в функции
def mysteries(tries_count: int):
    myst_dict = {
        "Кто проживает на дне океана?": ["Губка Боб", "Капитан Губка Боб", "Губка Боб Квадратные Штаны", "Спанч Боб"],
        "Где детонатор?": ["Где-то в Готэме", "Не помню", "Не знаю"],
        "Первое правило бойцовского клуба?": ["Не скажу", "Не знаю", "Спроси у Тайлера"]
    }
    for key, value in myst_dict.items():
        yield mystery(key, value, tries_count)
    print_dict()


def myst_tries(question: str, try_count: int):
    _result_dict[question] = try_count


def print_dict():
    [print(
        f"Загадка '{key}'\n{'Использовано попыток для верного ответа: ' + str(value) if value != 0 else 'Не разгадана'}\n")
        for key, value in _result_dict.items()]


if __name__ == '__main__':
    for tries in mysteries(5):
        print(f"Функция вернула: {tries}\n")
