import sys

local_task_db = []

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


def ask_for_continuation():
    if input("\n\nДля выхода введите любой символ.\nДля продолжения нажмите Enter...") != "":
        sys.exit()


def say_hello():
    print("\n📅 Добро пожаловать в планировщик задач! 🚩"
          "\nПрограмма умеет хранить ваши задачи, их дедлайны и уровень выполнения")


def get_tasks_count(complete_check: bool = False):
    if complete_check:
        complete_tasks_count = 0
        for task in local_task_db:
            if task[0] == 100:
                complete_tasks_count += 1

        return complete_tasks_count

    else:
        return len(local_task_db)


def delete_task():
    index = request_input("\nВведите номер задачи: ", int, range(1, len(local_task_db) + 1)) - 1
    local_task_db.pop(index)


def add_task():
    task_text = request_input("\nВведите текст задачи: ", str)
    task_deadline = request_input("Введите дедлайн для задачи: ", str)
    local_task_db.append([0, task_text, task_deadline])


def change_task_progress():
    if len(local_task_db) == 0: return
    index = request_input("\nВведите номер задачи: ", int, range(1, len(local_task_db) + 1)) - 1
    progress_level = request_input("Введите прогресс задачи: ", int)
    local_task_db[index][0] = progress_level


def get_average_progress():
    if len(local_task_db) == 0: return 100

    global_progress_level = 0

    for task in local_task_db:
        global_progress_level += task[0]

    return global_progress_level / len(local_task_db)


def get_summary():
    tasks_count = get_tasks_count()
    average_progress = get_average_progress()
    complete_tasks_count = get_tasks_count(True)
    return f"У вас сейчас {complete_tasks_count} выполненных задач из {tasks_count}, средний прогресс выполнения задач: {int(average_progress)}%"


def output_tasks():
    for task in local_task_db:
        print(f"{task[1]}: {task[0]} ({task[2]})")


def request_mode():
   return request_input("Выберите операцию:\n1 - Просмотреть текущие задачи\n2 - Добавить задачу\n3 - Изменить прогресс задачи\n4 - Удалить задачу\n ", int, range(1, 5))


def main():
    first_run = True
    say_hello()

    while True:
        if not first_run:
            ask_for_continuation()
            print("\n" * 50)
        else:
            first_run = False

        print(f"\n{get_summary()}\n")

        mode = request_mode()

        if mode == 1:
            output_tasks()
        elif mode == 2:
            add_task()
        elif mode == 3:
            change_task_progress()
        elif mode == 4:
            delete_task()

main()