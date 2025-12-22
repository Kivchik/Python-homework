def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

operations = ["+", "-", "*", "/"]

first = True
while True:
    if first:
        first = False
    else:
        print()
        input("Для продолжения нажмите Enter... ")

    print("\n" * 50)
    print("Доступные операции:")
    print("  \"+\" сложение")
    print("  \"-\" вычитание")
    print("  \"*\" умножение")
    print("  \"/\" деление")
    print()

    print("Для выхода введите: \"-1\"")
    operation = input("Введите операцию: ")

    if operation == "-1":
        break

    if operation not in operations:
        print("\033[31mОшибка: Такая операция не существует!\033[0m")
        continue

    num1 = input("Введите первое число: ")
    if not is_float(num1):
        print("\033[31mОшибка:", num1, "не является числом!\033[0m")
        continue
    else:
        num1 = float(num1)

    num2 = input("Введите первое число: ")
    if not is_float(num2):
        print("\033[31mОшибка:", num2, "не является числом!\033[0m")
        continue
    else:
        num2 = float(num2)

    answer = 0
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("\033[31mОшибка: Невозможно делить на ноль!\033[0m")
            continue
        else:
            answer = num1 / num2

    print("Ответ:", answer)

