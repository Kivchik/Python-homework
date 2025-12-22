"""
Билет 5

1. Теоретические вопросы:

1. Какие итерируемые объекты вы знаете?
2. Какой тип данных представляет логический тип?


2. Практические задания:

Практическую часть выполнять в IDE (VS Code) или онлайн-компиляторе.
Задание №1 Дан список “Yan”, “Kate” “Yana” “Elena”
Продемонстрируйте, как перебрать список с помощью циклов. (
Использовать все виды циклов)

Задание №2
Напишите функцию, которая вычисляет среднее арифметическое двух
чисел.


Теория:

1 - str, dict, list, set, frozenset и tuple

2 - bool
"""


# Практика:
# 1

my_list = ["Yan", "Kate", "Yana", "Elena"]
def iterate_by_for(lst):
    for item in lst:
        print(item)


def iterate_by_while(lst):
    index = 0
    while index < len(lst) - 1:
        print(lst[index])
        index = index + 1


iterate_by_while(my_list)
iterate_by_while(my_list)


# 2

def math_average_number(a, b):
    return (a + b) / 2
