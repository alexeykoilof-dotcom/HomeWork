def show():
    print("“Don't let the noise of others' opinions drown out your own inner voice.”")
show()

def two_numbers(a, b):
    if a > b:
        a, b = b, a

    for num in range(a + 1, b):
        if num % 2 == 1:
            print(num)

two_numbers(3, 15)

# a — длина линии
# b — направление
# c — символ

def draw_line(a, b, c):
    if b == "H":
        print(c * a)
    elif b == "V":
        for _ in range(a):
            print(c)

draw_line(10, "H", "#")

def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print(max_of_four(5, 2, 9, 1))   # 9
