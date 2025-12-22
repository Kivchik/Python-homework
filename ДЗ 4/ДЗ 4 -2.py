def imb_calculate(m, h):
    return m / ((h / 100)**2)

def str_convert(string):
    string = string.replace(" ", "")
    table = string.split(",")
    if len(table) == 2:
        return table
    else:
        return False

def imb_check(imb_index):
    if imb_index <= 18.5:
        return "Дефицит массы тела!"
    elif imb_index <= 24.9:
        return "Индекс в пределах нормы."
    elif imb_index <= 29.9:
        return "Избыточная масса тела."
    elif imb_index <= 34.9:
        return "Ожирение I степени!"
    elif imb_index <= 39.9:
        return "Ожирение II степени!!"
    elif imb_index > 39.9:
        return "Ожирение III степени!!!"

def main():
    while True:
        inpt = input(f"\nВведите ваш вес (КГ) и рост (СМ) через запятую: ")
        converted = str_convert(inpt)

        if converted:
            imb_index = imb_calculate(float(converted[0]), float(converted[1]))
            print(f"\nВаш индекс массы тела: {imb_index}")
            print(f"Статус индекса вашего тела: {imb_check(imb_index)}")    
        else:
            print(f"\nНеверный формат!")

main()