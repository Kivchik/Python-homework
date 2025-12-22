import json
import sys


def update_db(books_dict):
    with open('books.json', 'w') as books_db:
        json.dump(books_dict, books_db)


def get_db():
    try:
        with open('books.json', 'r', encoding='utf-8') as books_db:
            return json.load(books_db)
    except FileNotFoundError:
        return {}


def get_id_with_books(books_dict):
    id_and_books = {}
    for book_key, book in books_dict.items():
        id_and_books[book["id"]] = {"book": book, "key": book_key}

    return id_and_books


def generate_id(books_dict):
    books_id = get_id_with_books(books_dict).keys()
    if len(books_id) == 0:
        return 1

    for current_id in range(1, int(max(books_id)) + 2):
        if current_id not in books_id:
            return current_id

    return False


def check_and_fix_formation_of_db(books_dict):
    base_book_formation = {
        "author": "Неизвестно",
        "title": "Неизвестно",
        "year": "Неизвестно",
        "status": "Неизвестно",
        "description": "Неизвестно",
    }

    for book in books_dict.values():
        for key, default_value in base_book_formation.items():
            book.setdefault(key, default_value)



def add_book(books_dict, title, author, year, description):
    key = f"{title}::{author}"
    if key in books_dict:
        return False

    book_id = generate_id(books_dict)
    books_dict[key] = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "status": "В наличии",
        "description": description,
    }

    return True


def find_books(books_dict, request):
    request_lower = str(request).lower()
    response_frm_db = {}
    for book_key, book in books_dict.items():
        for key, value in book.items():
            if request_lower in str(value).lower():
                if key not in response_frm_db:
                    response_frm_db[key] = {}
                response_frm_db[key][book_key] = book
    if len(response_frm_db) == 0:
        return False

    return response_frm_db


def borrow_book_by_id(books_dict, book_id):
    book_and_key = get_id_with_books(books_dict)[book_id]
    if str.lower(book_and_key["book"]["status"]) == "выдана":
        return False
    else:
        books_dict[book_and_key["key"]]["status"] = "Выдана"

    return True


def return_book_by_id(books_dict, book_id):
    book_and_key = get_id_with_books(books_dict)[book_id]
    if str.lower(book_and_key["book"]["status"]) == "в наличии":
        return False
    else:
        books_dict[book_and_key["key"]]["status"] = "В наличии"

    return True


def get_available_books(books_dict):
    available_books = {}
    for book_key, book in books_dict.items():
        if str.lower(book["status"]) == "в наличии":
            available_books[book_key] = book

    return available_books


def print_books(books_dict):
    if len(books_dict) == 0:
        return False

    return_text = "\n\n══════════════════ஜ▲ஜ══════════════════"
    for book_key, book in books_dict.items():
        return_text += (f"\n\n       📖 Книга \"{book["title"]}\""
                        f"\n       🖋 Автор: {book["author"]}"
                        f"\n       📅 Год выпуска: {book["year"]}"
                        f"\n       📦 Статус: {book["status"]}"
                        f"\n       🔧 id: {book["id"]}\n"
                        f"\n════════════════════════════════════════")

    print(f"{return_text}\n")
    return True


def say_hello_ui():
    print("📖 Добро пожаловать в систему учёта книг! 💾")


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


def delete_book(books_dict, book_id):
    book_key = get_id_with_books(books_dict)[book_id]["key"]

    if book_key in books_dict:
        books_dict.pop(book_key)
        update_db(books_dict)
        return True
    else:
        return False


def search_tool_ui(books_dict):
    request = request_input("\n🔎 Введите поисковой запрос\n\n> ", str)
    search_result = find_books(books_dict, request)
    if not search_result:
        print("\n❌ Ничего не найдено")
    else:
        print()
        for search_type, result in search_result.items():
            print(f"✔ Найдено {len(search_result[search_type])} книг, по {search_type}")

        if len(search_result) == 1:
            print_books(list(search_result.values())[0])
        else:
            view_category = request_input("\nВведите желаемый тип совпадений (написано на латинице ↑)\n\n> ", str, search_result.keys())
            print_books(search_result[view_category])


def add_tool_ui(books_dict):
    title = request_input("\nВведите название книги: ", str)
    author = request_input("Введите имя автора: ", str)
    year = request_input("Введите год выпуска: ", int)
    description = request_input("Введите описание книги: ", str)

    operation_status = add_book(books_dict, title, author, year, description)
    if operation_status:
        print("\n✔ Книга успешно добавлена")
    else:
        print("\n❌ Не удалось добавить книгу")

    update_db(books_dict)


def request_book_id_ui(books_dict):
    while True:
        book_id = request_input("\nВведите id книги: ", int)
        if book_id not in get_id_with_books(books_dict).keys():
            print("\n❌ Книги с таким id не существует")
        else:
            break

    return book_id


def status_tool_ui(books_dict):
    action_index = request_input("\n   1 - Выдать книгу\n   2 - Вернуть книгу\n\n> ", str)
    book_id = request_book_id_ui(books_dict)

    action_status = None
    if action_index == "1":
        action_status = borrow_book_by_id(books_dict, book_id)
    elif action_index == "2":
        action_status = return_book_by_id(books_dict, book_id)

    if action_status:
        print("\n✔ Статус успешно изменён")
    else:
        print("\n❌ Книга уже имеет указанный статус")

    update_db(books_dict)


def delete_tool_ui(books_dict):
    book_id = request_book_id_ui(books_dict)
    print("Книга которую вы хотите удалить:")
    print_books({"temp_key": list(books_dict.values())[0]})
    confirmation = request_input("Вы уверены что хотите удалить эту книгу? (да / нет)\n\n> ", str, ["да", "нет", "Да", "Нет"])

    operation_status = None
    if str.lower(confirmation) == "да":
        operation_status = delete_book(books_dict, book_id)

    if operation_status:
        print("\n✔ Книга успешно удалена")
        update_db(books_dict)
    else:
        print("\n❌ Не удалось удалить книгу или операция была отменена")


def available_books_ui(books_dict):
    available_books = get_available_books(books_dict)
    books_count = len(available_books)
    if books_count > 0:
        print(f"\n✔ Количество книг в наличии: {books_count}")
        print_books(available_books)
    else:
        print("\n❌ Нет книг в наличии")


def all_books_ui(books_dict):
    books_count = len(books_dict)
    if books_count > 0:
        print(f"\n✔ Количество зарегистрированных книг: {books_count}")
        print_books(books_dict)
    else:
        print("\n❌ В системе нет книг!")


def change_book_element_by_id(books_dict, book_id, key, new_content):
    book_key = get_id_with_books(books_dict)[book_id]["key"]
    books_dict[book_key][key] = new_content

    update_db(books_dict)


def change_book_element_ui(books_dict):
    book_id = request_book_id_ui(books_dict)
    book = get_id_with_books(books_dict)[book_id]["book"]

    available_actions_text = ("\nПожалуйста, выберите пункт для изменения:"
                              "\n   1 - Название"
                              "\n   2 - Автор"
                              "\n   3 - Год выпуска"
                              "\n   4 - Описание"
                              "\n\n> ")

    selected_action_index = request_input(available_actions_text, int, range(1, 5)) - 1

    key_and_type_by_index = [["title", str], ["author", str], ["year", int], ["description", str]]
    key = key_and_type_by_index[selected_action_index][0]
    content_type = key_and_type_by_index[selected_action_index][1]
    book[key] = book.get(key, "")
    new_content = request_input(f"\nСтарое содержание пункта:\n  {book[key]}\n\nВведите новое содержание пункта\n\n> ", content_type)

    change_book_element_by_id(books_dict, book_id, key, new_content)

    print("\n✔ Пункт книги успешно изменён")


def print_book_description(book_dict):
    book_id = request_book_id_ui(book_dict)
    book_description = get_id_with_books(book_dict)[book_id]["book"]["description"]
    print(f"\nОписание выбранной книги:\n{book_description}")


def actions_selector_ui(books_dict):
    available_actions_text = ("\nПожалуйста, выберите желаемое действие:"
                              "\n   1 - 📚 Просмотреть все книги "
                              "\n   2 - 📦 Посмотреть книги в наличии"
                              "\n   3 - 🔎 Поиск книг"
                              "\n   4 - 📖 Прочитать описание книги"
                              "\n   5 - ➕ Добавить новую книгу"
                              "\n   6 - 📂 Изменить статус книги"
                              "\n   7 - 🖋 Изменить книгу"
                              "\n   8 - 💣 Удалить книгу"
                              "\n\n   9 - 🔚 Завершить программу"
                              "\n\n> ")

    selected_action_index = request_input(available_actions_text, int, range(1, 10))

    if selected_action_index == 1:
        all_books_ui(books_dict)
    elif selected_action_index == 2:
        available_books_ui(books_dict)
    elif selected_action_index == 3:
        search_tool_ui(books_dict)
    elif selected_action_index == 4:
        print_book_description(books_dict)
    elif selected_action_index == 5:
        add_tool_ui(books_dict)
    elif selected_action_index == 6:
        status_tool_ui(books_dict)
    elif selected_action_index == 7:
        change_book_element_ui(books_dict)
    elif selected_action_index == 8:
        delete_tool_ui(books_dict)
    elif selected_action_index == 9:
        sys.exit()


def ask_for_continuation_ui():
    if input("\n\nДля выхода введите любой символ.\nДля продолжения нажмите Enter...\n\n> ") != "":
        sys.exit()


def main():
    books_db_value = get_db()
    check_and_fix_formation_of_db(books_db_value)

    print("\n" * 50)
    say_hello_ui()

    while True:
        actions_selector_ui(books_db_value)
        ask_for_continuation_ui()
        print("\n"*50)

main()