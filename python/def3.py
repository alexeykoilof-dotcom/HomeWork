def max_in_list(lst):
    # Базовый случай: если в списке один элемент
    if len(lst) == 1:
        return lst[0]

    # Рекурсивно находим максимум в остатке списка
    max_rest = max_in_list(lst[1:])

    # Сравниваем первый элемент с максимумом остатка
    if lst[0] > max_rest:
        return lst[0]
    else:
        return max_rest


# Пример использования
print(max_in_list([3, 8, 1, 9, 2, 7]))  # → 9


def partitions(n, max_num=None):
    if max_num is None:
        max_num = n

    if n == 0:
        return [[]]  # одно пустое разбиение

    result = []

    for i in range(1, min(n, max_num) + 1):
        # Берём число i, а остаток n-i разбиваем с числами ≤ i
        for p in partitions(n - i, i):
            result.append([i] + p)

    return result


# Пример для числа 4
for p in partitions(4):
    print(p)