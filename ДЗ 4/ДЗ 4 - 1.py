
def rectangle_area(width, height):
    return width * height

def str_convert(string):
    string = string.replace(" ", "")
    table = string.split(",")
    if len(table) == 2:
        return table
    else:
        return False

def main():
    while True:
        inpt = str(input(f"\nВведите ширину и высоту прямоугольника через запятую: "))
        converted = str_convert(inpt)

        if converted:
            print(f"\nПлощадь данного прямоугольника: {rectangle_area(int(converted[0]), int(converted[1]))}")
        else:
            print(f"\nНеверный формат!")

main()
