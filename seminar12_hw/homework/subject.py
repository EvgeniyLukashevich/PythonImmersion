__all__ = ['Subject']


class Subject:
    def __init__(self, name):
        self.name = name
        self.scores = []
        self.test_results = []

    def add_score(self, score):
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.scores.append(score)

    def add_test_result(self, result):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.test_results.append(result)

    def get_average_score(self):
        if not self.scores:
            return 0
        return round(sum(self.scores) / len(self.scores), 2)

    def get_average_test_result(self):
        if not self.test_results:
            return 0
        return round(sum(self.test_results) / len(self.test_results), 2)
