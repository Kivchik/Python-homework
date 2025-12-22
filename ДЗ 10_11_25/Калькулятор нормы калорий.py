import sys

def request_input(request_text, expected_type, expected_values=None):
    while True:
        user_input = input(request_text)

        try:
            value = expected_type(user_input)
        except ValueError:
            continue

        if expected_values is not None:
            if value not in expected_values:
                continue

        return value



def calculate_basic_metabolism(weight, height, age, sex):
    amendment = {"м": 5, "ж": -161}
    return weight * 10 + height * 6.25 - age * 5 + amendment[sex]


def output_list(input_list, print_index = False, index_separator = " - ", line_separator = False):
    for i in range(0, len(input_list)):
        if print_index:
            print(f"{i}{index_separator}{input_list[i]}")
        else:
            print(input_list[i])

        if line_separator and i != len(input_list):
            print(line_separator)


def say_hello():
    print("\n🍔 Добро пожаловать в программу подсчёта нормы калорий! 🥤"
          "\nПрограмма умеет подсчитывать калории, учитывая ваш возраст, пло, образ жизни и телосложение.")


def ask_for_continuation():
    if input("\n\nДля выхода введите любой символ.\nДля продолжения нажмите Enter...") != "":
        sys.exit()


activity_index_example = [
    "1.2: Сидячий образ жизни (мало или нет упражнений).",
    "1.375: Легкая активность (легкие упражнения 1-3 дня в неделю).",
    "1.55: Умеренная активность (умеренные упражнения 3-5 дней в неделю).",
    "1.725: Высокая активность (интенсивные упражнения 6-7 дней в неделю).",
    "1.9: Очень высокая активность (очень интенсивные упражнения, физический труд).",
]


def main():
    first_run = True
    say_hello()

    while True:
        if not first_run:
            ask_for_continuation()
            print("\n" * 50)
        else:
            first_run = False

        sex = request_input("\nВведите свой пол (м / ж): ", str, ["м", "ж", "М", "Ж"])
        age = request_input("Введите свой возраст: ", float)
        weight = request_input("Введите свой вес (КГ): ", float)
        height = request_input("Введите свой рост (СМ): ", float)

        basic_metabolism = calculate_basic_metabolism(weight, height, age, sex)

        print("\nПримеры уровня дневной активности:")
        output_list(activity_index_example)
        activity_level = request_input("\nПожалуйста, введите ваш уровень дневной активности: ", float)

        recomended_dayly_calories = basic_metabolism * activity_level

        print(f"\nВаша норма калорий в день: {recomended_dayly_calories}ккал\nПриятного аппетита!")


main()
