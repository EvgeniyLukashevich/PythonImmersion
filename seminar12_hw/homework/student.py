import csv
from seminar12_hw.homework.subject import Subject

__all__ = ['Student']


class FIODescriptor:
    def __get__(self, instance, owner):
        return instance._fio

    def __set__(self, instance, value: str):
        for name in value.split(' '):
            if not name.istitle() or not name.isalpha():
                raise ValueError(
                    "Фамилия, Имя и Отчество должны начинаться с заглавной буквы и состоять только из букв")
        instance._fio = value


class Student:
    __fio = FIODescriptor()
    __subjects_file = "subjects.csv"

    def __init__(self, fio):
        self.__fio = fio
        self.subjects = self.__load_subjects()

    @property
    def name(self):
        return self.__fio

    def __load_subjects(self):
        subjects = {}
        with open(self.__subjects_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                subject_name = row[0]
                subjects[subject_name] = Subject(subject_name)
        return subjects

    def add_score(self, subject_name: str, *args: int):
        if subject_name not in self.subjects:
            raise ValueError("Нет такого предмета :(")
        for score in args:
            self.subjects[subject_name].add_score(score)

    def add_test_result(self, subject_name: str, *args: int):
        if subject_name not in self.subjects:
            raise ValueError("Нет такого предмета :(")
        for result in args:
            self.subjects[subject_name].add_test_result(result)

    def get_average_score(self, subject_name: str):
        if subject_name not in self.subjects:
            raise ValueError("Нет такого предмета :(")
        return self.subjects[subject_name].get_average_score()

    def get_average_test_result(self, subject_name: str):
        if subject_name not in self.subjects:
            raise ValueError("Нет такого предмета :(")
        return self.subjects[subject_name].get_average_test_result()

    def get_overall_average_score(self):
        if not self.subjects:
            return 0
        total_score = 0
        count = 0
        for subject in self.subjects.values():
            if subject.get_average_score() == 0:
                continue
            total_score += subject.get_average_score()
            count += 1
        return round(total_score / count, 2)

    def __str__(self):
        text = self.__fio
        for subject_key, subject_value in self.subjects.items():
            text += f'\n{subject_key}' \
                    f'\n  Оценки: {subject_value.scores}' \
                    f'\n  Средняя оценка: {self.get_average_score(subject_key)}' \
                    f'\n  Тесты: {subject_value.test_results}' \
                    f'\n  Средний балл за тесты: {self.get_average_test_result(subject_key)}\n'
        text += f'\nОбщий средний балл: {self.get_overall_average_score()}'
        return text
