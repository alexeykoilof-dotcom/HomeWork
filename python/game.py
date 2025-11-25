def start_game():
    print("\n-ТОПОВАЯ ИГРА-")
    print("\nВы стоите перед колледжом.")
    print("\n1. Войти в колледж")
    print("2. Обойти колледж")
    print("3. Пойти домой")

    choice = input("\nВыбор (1 или 3): ")

    if choice == "1":
        inside_house()
    elif choice == "2":
        around_house()
    elif choice == "3":
        go_home()
    else:
        print("Неверный выбор")
        start_game()  # Начать заново

def go_home():
    print("ВАС ОТЧИСЛИЛИ!!! XDDDD")


def inside_house():
    print("\nВы вошли в колледж!!! Здесь две комнаты.")
    print("1. Пойти налево")
    print("2. Пойти направо")

    choice = input("\nВыбор (1 или 2): ")

    if choice == "1":
        print("\nВЫ ЗАКРЫЛИ СЕССИЮ! Победа!")
    elif choice == "2":
        print("\nВАС ОТЧИСЛИЛИ! Поражение")
    else:
        inside_house()


def around_house():
    print("\nВы обошли колледж и нашли Андрея.")
    print("1. Попросить помочь, узнать что такое print")
    print("2. Купить у Андрея зачёт по предмету")

    choice = input("\nВаш выбор (1 или 2): ")

    if choice == "1":
        print("\nВы сдали зачёт!")
        print("ПОБЕДА!")
    else:
        print("\n1ВАС ОТЧИСЛИЛИ!))0")


# ЗАПУСК ИГРЫ
start_game()