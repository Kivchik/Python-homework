def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

first = True
while True:
    if first:
        first = False
    else:
        print()
        input("Для продолжения нажмите Enter... ")

    print("\n" * 50)
    print("Для выхода введите: \"-1\"")
    num1 = input("Введите первое число: ")
    if num1 == "-1":
        break
    if not is_float(num1):
        print("Ошибка:", num1, "- не число!")
        continue

    num2 = input("Введите второе число: ")
    if num1 == "-1":
        break
    if not is_float(num2):
        print("Ошибка:", num2, "- не число!")
        continue

    if num1 > num2:
        print(num1, "больше", num2)
    elif num1 < num2:
        print(num2, "больше", num1)
    else:
        print(num1, "и", num2, "равны")