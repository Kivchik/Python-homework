# Теория
# 1 - Метод insert относится к типу данных list, он позволяет вставить данные по указанному индексу,
#     все элементы начиная с указанного индекса вправо
#     Синтаксис: <list name>.insert(<index>, <item>)

# 2 - Методы типов данных нужны для упрощения работы с ними, на примере метода index, относящегося к типу list,
#     можно понять их полезность:

new_list = [1,2,3,4,5,6,7,8,9]
# Работа через метод:
new_list.index(3) # --> Вернёт 2, найдя число 3 по индексу 2

def index_in_list(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i

index_in_list(new_list, 3) # --> Точно также вернёт индекс 2, но уже существует метод index, так что методы нужны
# для упрощения работы с данными и переменными

# Практика
# 1
def insert_in_list(lst, index, item):
    length = len(lst)
    if index <= length - 1:
        return lst[:index - length] + [item] + lst[index:]
    else:
        return lst + [item]

# 2
def calculator(num1, action, num2):
    result = None
    if action == "+":
        result = num1 + num2
    elif action == "-":
        result = num1 - num2
    elif action == "*":
        result = num1 * num2
    elif action == "/":
        if num2 == 0:
            raise ZeroDivisionError
        else:
            result = num1 / num2

    return result
