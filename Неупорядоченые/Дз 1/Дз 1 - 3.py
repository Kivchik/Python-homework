print("Введите \"выход\", что бы завершить программу")
print()

while True:
    Len = input("Введите расстояние в километрах: ")
    if Len == "выход":
        break

    Len = int(Len)
    M = Len * 1000
    Mil = Len * 0.62

    print()
    print("В метрах:", M)
    print("В милях:", Mil)

