print("Введите \"выход\", что бы завершить программу")

while True:
    Cels = input("Введите температуру в цельсиях: ")
    if Cels == "выход":
        break

    Cels = int(Cels)
    F = Cels * 9 / 5 + 32
    K = Cels + 273.15

    print()
    print("Температура в фаренгейтах:", F)
    print("Температура в кельвинах", K)

    