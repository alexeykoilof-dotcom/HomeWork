# Задание 1
a = int(input())
b = int(input())
c = int(input())
print(a * 100 + b * 10 + c)

# Задание 2
n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(a * b * c * d)

# Задание 3
m = int(input())
print(m * 100)        # сантиметры
print(m * 10)         # дециметры
print(m * 1000)       # миллиметры
print(m * 0.000621371)  # мили

# Задание 4
a = int(input())
h = int(input())
print((a * h) / 2)

# Задание 5
n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(d * 1000 + c * 100 + b * 10 + a)