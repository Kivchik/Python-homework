# 1
films = ["Интерстеллар", "Космическая одессея 2010", "Марсианин", "Салют-7", "Тайна красной планеты"]

# 2
films.append("Игра Эндера")

# 3
films.insert(1, "2012")

# 4
films.pop(len(films) - 1)

#5
print(films[2])

#---------------------------------------------------------------------------------------------------------------

numbers = [12, 45, 23, 67, 34, 89, 12, 45, 67, 23]

# 1
def get_uniq_items(array):
    numbers_counter = {}
    for item in array:
        numbers_counter[item] = numbers_counter.get(item, 0) + 1

    uniq_items = []
    for key, value in numbers_counter.items():
        if value == 1:
            uniq_items.append(key)

    return uniq_items

uniq_numbers = get_uniq_items(numbers)
print(len(get_uniq_items(numbers)))

# 2
# Уже найдены выше
print(uniq_numbers)

# 3
uniq_numbers.sort(reverse=True)
print(uniq_numbers)

# 4
# Уже отсортированы по убыванию, так что просто берём 3 первые числа
print(uniq_numbers[:3])

#---------------------------------------------------------------------------------------------------------------

students = ["Борис", "Анна", "Виктория", "Григорий", "Дарья", "Евгений", "Жанна"]

# 1
first_three = students[:3]

# 2
last_three = students[-3:]

#---------------------------------------------------------------------------------------------------------------

def analyze_list(array):
    """
    Анализирует список чисел и возвращает статистику
    """

    return_dict = {}

    return_dict["sum"] = sum(array)
    return_dict["average"] = sum(array) / len(array)
    return_dict["max"] = max(array)
    return_dict["min"] = min(array)

    return return_dict

test_numbers = [1, 2, 3, 4, 5]
result = analyze_list(test_numbers)
print(result)

