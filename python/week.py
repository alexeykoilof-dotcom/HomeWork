# Программа учёта времени учёбы за неделю
# Автор: ваш помощник :)

print("=== Учёт времени учёбы за неделю ===")

# 1. Запрашиваем количество учебных дней (от 1 до 7)
while True:
    try:
        days = int(input("\nВведите количество учебных дней (от 1 до 7): "))
        if 1 <= days <= 7:
            break  # всё правильно — выходим из цикла
        else:
            print("Ошибка! Количество дней должно быть от 1 до 7.")
    except ValueError:
        print("Ошибка! Введите целое число.")

# 2. Список для хранения часов по дням
hours_list = []

# 3. Цикл для ввода часов за каждый день
for day in range(1, days + 1):
    while True:
        try:
            hours = float(input(f"Сколько часов вы учились в день {day}? "))
            if hours >= 0:
                hours_list.append(hours)
                break  # корректный ввод — переходим к следующему дню
            else:
                print("Ошибка! Количество часов не может быть отрицательным.")
        except ValueError:
            print("Ошибка! Введите число (например, 3 или 2.5).")

# 4. Подсчёт и вывод общего времени
total_hours = sum(hours_list)

print("\n" + "*"*40)
print("РЕЗУЛЬТАТ ЗА НЕДЕЛЮ")
print("*"*40)
for i in range(days):
    print(f"День {i+1}: {hours_list[i]} ч.")
print("-" * 40)
print(f"Всего часов учёбы: {total_hours} ч.")
print("="*40)

# Дополнительно — приятный вывод
if total_hours >= 20:
    print("Отличная работа!")
elif total_hours >= 10:
    print("Неплохо!")
else:
    print("Можно и побольше!")