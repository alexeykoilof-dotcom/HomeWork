expression = input()

operators = ['+', '-', '*', '/']

operator = ''
operator_index = -1
for op in operators:
    if op in expression:
        operator = op
        operator_index = expression.find(op)
        break

if operator_index != -1:
    num1_str = expression[:operator_index]
    num2_str = expression[operator_index + 1:]

    num1 = float(num1_str)
    num2 = float(num2_str)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: Деление на ноль"

    print(f"Результат: {result}")
else:
    print("Ошибка.")

#задание 2

    import random

    list_size = 20
    min_value = -50
    max_value = 50

    random_list = [random.randint(min_value, max_value) for _ in range(list_size)]

    negative_count = 0
    positive_count = 0
    zero_count = 0

    for number in random_list:
        if number < 0:
            negative_count += 1
        elif number > 0:
            positive_count += 1
        else:
            zero_count += 1

    print(f"Исходный список: {random_list}")

    print(f"Минимальный элемент: {min(random_list)}")
    print(f"Максимальный элемент: {max(random_list)}")
    print(f"Количество отрицательных: {negative_count}")
    print(f"Количество положительных: {positive_count}")
    print(f"Количество нулей: {zero_count}")