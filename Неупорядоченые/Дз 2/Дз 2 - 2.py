def check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                 return True
            else:
                return False
        else:
            return True
    else:
        return False

def check2(year):
    try:
        int(year)
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
    year = input("Введите год: ")

    if year == "-1":
        break

    if len(year) != 4 or not check2(year):
        print("Не верный формат года!")
        continue

    if check(int(year)):
        print(year, "- високосный год")
    else:
        print(year, "- не високосный год")