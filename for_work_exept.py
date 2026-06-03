while True:
    try:
        user_input = input("Введите целое число: ")

        number = int(user_input)

        print("Вы ввели число:", number)
        break

    except ValueError:
        print("Невозможно преобразовать введенное значение в целое число")
        print("Попробуйте еще раз.\n")

    except TypeError:
        print("Введено значение неподходящего типа")
        print("Попробуйте еще раз.\n")