__all__ = ['MysteryGame']


class MysteryGame:
    __MYSTERIES_DICT = {
        "Кто проживает на дне океана?": ["Губка Боб", "Капитан Губка Боб", "Губка Боб Квадратные Штаны", "Спанч Боб"],
        "Где детонатор?": ["Где-то в Готэме", "Не помню", "Не знаю"],
        "Первое правило бойцовского клуба?": ["Не скажу", "Не знаю", "Спроси у Тайлера"]
    }

    def __init__(self, tries_count: int = 3):
        self.tries_count = tries_count
        self._result_dict = dict()

    def start(self):
        for tries in self.__mysteries(self.tries_count):
            print(f" Код: {tries}\n")

    def __mystery(self, question: str, answers: list) -> int:
        current_try = 0
        print("\n# # # # # # # # # # # # # #\n")
        print(f"Загадка. {question}")

        while current_try < self.tries_count:

            if input("Твой вариант ответа: ") in answers:
                current_try += 1
                self.__myst_tries(question, current_try)
                print(f"Верно! Тебе понадобилось попыток: {current_try}\n")
                return current_try

            else:
                current_try += 1
                print(f"\nНеверно! Попыток осталось: {self.tries_count - current_try}")

        print(f"К сожалению попытки закончились! Верный ответ: {answers[0]}\n")
        self.__myst_tries(question, self.tries_count - current_try)
        return self.tries_count - current_try

    def __myst_tries(self, question: str, try_count: int):
        self._result_dict[question] = try_count

    def __print_dict(self):
        print("\n# # # # # # # # # # # # # #\n")
        [print(
            f"Загадка '{key}'\n{'Использовано попыток для верного ответа: ' + str(value) if value != 0 else 'Не разгадана'}\n")
            for key, value in self._result_dict.items()]
        print("\n# # # # # # # # # # # # # #\n")

    def __mysteries(self, tries_count: int):
        for key, value in self.__MYSTERIES_DICT.items():
            yield self.__mystery(key, value)
        self.__print_dict()

