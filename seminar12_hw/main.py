from homework import *

student = Student("Иванов Иван Иванович")

student.add_score("Математика", 5, 3, 4, 2, 4)
student.add_test_result("Математика", 98, 55, 77)

student.add_score("Физика", 3, 4, 3)
student.add_test_result("Физика", 80, 32, 57)

student.add_score("Химия", 5, 5, 5, 2, 2)
student.add_test_result("Химия", 75, 85, 45)

student.add_score("Биология", 4, 4, 5, 3)
student.add_test_result("Биология", 22, 32, 42, 54)

print(student)
