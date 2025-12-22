X = 10
def print_x():
    print(X)

print(f"↓ X = {X}. Результат работы простейшей функции: вывела X ↓")
print_x()


input(f"\n Для продолжения нажмите Enter...")
print(f"\n" * 30)


error = "Ошибка! Вы скопировали ДЗ из нейросети!"
def print_error(error_str):
    print(f"\033[31m{error_str}\033[0m")


print(f"↓ Работа функции с принимаемым атрибутом ↓ "
      f"\n Входной атрибут: \"{error}\" "
      f"\n ↓ Результат работы функции: вывела ошибку красным цветом ↓")
print_error(error)


input(f"\n Для продолжения нажмите Enter...")
print(f"\n" * 30)


def power(x, y):
    return x ** y

x = 2
y = 3
answer = power(2, 3)
print(f"↓ Работа функции с принимаемым атрибутом ↓ "
      f"\n Входные атрибуты: x = {x} и y = {y}"
      f"\n ↓ Результат работы функции ↓ "
      f"\n Вернула {x} в степени {y}: {answer}")

