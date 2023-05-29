# Пользователь вводит данные.
# Сделайте проверку данных и, если возможно,
# преобразуйте в один из вариантов ниже:
#  - Целое положительное число
#  - Вещественное положительное или отрицательное число
#  - Строку в нижнем регистре, если в троке есть хотя бы одно заглавная буква
#  - Строку в нижнем регистре в остальных случаях

def converting(user_input: str):
    if user_input.isnumeric() and int(user_input) > 0:
        print("Пользователь ввел целое положительное число:", user_input)
        return int(user_input)

    elif "." in user_input and (float(user_input) < 0 or float(user_input)) > 0:
        print("Пользователь ввел вещественное число:", user_input)
        return float(user_input)

    else:
        for char in user_input:
            if char.isupper():
                print("Во вводе пользователя есть хотя бы одна заглавная буква:", user_input)
                return user_input.lower()
        print("Данные попали в разряд 'остальные случаи':", user_input)
        return user_input.lower()


user_input = input("Пожалуйста введите данные: ")
converted_input = converting(user_input)
print("Преобразованные данные:", converted_input)
