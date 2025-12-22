import datetime
import json
import sys


def correct_year(year: int):
    now = datetime.datetime.now().year
    if year > now:
        return now
    else:
        return year


def auto_list_ui(auto_list: list, supported_parameters: dict = None, top_label: str = None, empty_error_text: str = None, spaces: int = 3, key_val_spacer: str = ": ", min_interface_len: int = 0, second_top_label: str = None):
        if len(auto_list) == 0:
            auto_list_ui([empty_error_text])
            return

        max_text_len = min_interface_len
        if top_label and len(top_label) > max_text_len:
            max_text_len = len(top_label)

        if second_top_label and len(second_top_label) > max_text_len:
            max_text_len = len(second_top_label)

        for i in range(len(auto_list)):
            if type(auto_list[i]) == dict or type(auto_list[i]) == set:
                for parameter, value in auto_list[i].items():
                    if supported_parameters:
                        text_len = len(supported_parameters[parameter] + str(value)) + 2
                    else:
                        text_len = len(str(parameter) + str(value)) + 2

                    if max_text_len < text_len:
                        max_text_len = text_len

            elif type(auto_list[i]) == list or type(auto_list[i]) == tuple:
                for item in auto_list[i]:
                    text_len = 0
                    try:
                        text = str(item)
                    except ValueError:
                        continue
                    text_len += len(text)
                    if max_text_len < text_len:
                        max_text_len = text_len

            else:
                text_len = 0
                try:
                    str(auto_list[i])
                    text_len = len(str(auto_list[i]))
                except ValueError:
                    pass

                if max_text_len < text_len:
                    max_text_len = text_len

        max_text_len += spaces * 2
        print_text = f"\n\n╔{"═" * max_text_len}╗"

        if top_label:
            pre_top_label_len = (max_text_len / 2) - (len(top_label) / 2)
            post_top_label_len = pre_top_label_len
            if pre_top_label_len % 1 != 0:
                post_top_label_len += 1

            post_top_label_len = int(post_top_label_len)
            pre_top_label_len = int(pre_top_label_len)
            print_text += f"\n║{" " * pre_top_label_len}{top_label}{" " * post_top_label_len}║\n╠{"═" * max_text_len}╣"

        if second_top_label:
            pre_top_label_len = (max_text_len / 2) - (len(second_top_label) / 2)
            post_top_label_len = pre_top_label_len
            if pre_top_label_len % 1 != 0:
                post_top_label_len += 1

            post_top_label_len = int(post_top_label_len)
            pre_top_label_len = int(pre_top_label_len)
            print_text += f"\n║{" " * pre_top_label_len}{second_top_label}{" " * post_top_label_len}║\n╠{"═" * max_text_len}╣"

        print_text += f"\n║{" " * max_text_len}║"

        def text_gen(text):
            return f"\n║{" " * spaces}{text}{" " * (max_text_len - spaces - len(text))}║"

        for i in range(len(auto_list)):
            if type(auto_list[i]) == dict:
                for parameter, value in auto_list[i].items():
                    if supported_parameters:
                        parameter = supported_parameters[parameter]
                    if parameter:
                        print_text += text_gen(f"{parameter}{key_val_spacer}{value}")

            elif type(auto_list[i]) == list or type(auto_list[i]) == tuple or type(auto_list[i]) == set:
                for item in auto_list[i]:
                    try:
                        print_text += text_gen(f"{item}")
                    except ValueError:
                        pass

            else:
                try:
                    print_text += text_gen(f"{auto_list[i]}")
                except ValueError:
                    pass

            if i != len(auto_list) - 1:
                print_text += f"\n║{" " * max_text_len}║\n╠{"═" * max_text_len}╣\n║{" " * max_text_len}║"
            else:
                print_text += f"\n║{" " * max_text_len}║\n╚{"═" * max_text_len}╝"

        print(print_text)


def request_input(request_text: str, expected_type: type, expected_values: list = None, attempts: int = 999, error_text: str = None):
    for i in range(attempts):
        user_input = input(request_text)

        try:
            user_input = expected_type(user_input)
        except ValueError:
            if error_text:
                print(error_text)
            continue

        if expected_values and user_input in expected_values:
            return user_input
        elif not expected_values:
            return user_input
        else:
            print(error_text)

    return False


def request_input_with_auto_list(request_text: str, expected_type: type, expected_values: list = None, attempts: int = 999, error_text: str = None, input_marker = "\n\n> "):
    for i in range(attempts):
        auto_list_ui([request_text])
        user_input = input(input_marker)

        try:
            user_input = expected_type(user_input)
        except ValueError:
            if error_text:
                auto_list_ui([error_text])
            continue

        if expected_values and user_input in expected_values:
            return user_input
        elif not expected_values:
            return user_input
        else:
            auto_list_ui([error_text])

    return False


def selector(items_list: list, request_text: str = "", pre_item_text: str = "   ", spacer: str = " - ", post_item_text:str = ""):
    request_text = request_text
    for i in range(len(items_list)):
        request_text += f"\n{pre_item_text}{i+1}{spacer}{items_list[i][0]}{post_item_text}"

    request_text += "\n\n> "
    user_input = request_input(request_text, int, range(1, len(items_list) + 1)) - 1

    return items_list[user_input][1]


def selector_with_auto_list(items_list: list, request_text: str = None, pre_item_text: str = "", spacer: str = " - ", post_item_text:str = "", top_label: str = None, second_top_label: str = None):
    request_list = [[]]
    for i in range(len(items_list)):
        request_list[0].append(f"{pre_item_text}{i+1}{spacer}{items_list[i][0]}{post_item_text}")

    auto_list_ui(request_list, request_text, top_label = top_label, second_top_label = second_top_label)
    user_input = request_input("\n\n> ", int, range(1, len(items_list) + 1)) - 1

    return items_list[user_input][1]


class DB:
    def __init__(self, db_path: str = "db.json"):
        self.OriginDB = []
        self.IndexedDB = {
            "cid": {},
            "producer": {},
            "model": {},
            "year": {},
            "status": {},
            "price": {},
        }
        self.DBPath = db_path
        self.Settings = {
            "Soft search": True,
        }
        self.SpacedCIDList = []

        self.import_db()
        self.index_db()

    def import_db(self):
        try:
            with open(self.DBPath, 'r', encoding='utf-8') as f:
                db_list = json.load(f)
        except FileNotFoundError:
            self.OriginDB = []
            return

        self.OriginDB = db_list

    def export_db(self):
        with open(self.DBPath, 'w') as f:
            json.dump(self.OriginDB, f)

    def index_db(self) -> bool:
        self.IndexedDB = {
            "cid": {},
            "producer": {},
            "model": {},
            "year": {},
            "status": {},
            "price": {},
        }

        if len(self.OriginDB) == 0:
            return False

        for i in range(len(self.OriginDB)):
            self.index_item(self.OriginDB[i], i)

        for i in range(max(self.IndexedDB["cid"])):
            if i + 1 not in self.IndexedDB:
                self.SpacedCIDList.append(i + 1)

        return True

    def index_item(self, item, origin_index):
        for index in self.IndexedDB.keys():
            if item[index] and index != "cid":
                self.IndexedDB[index][item[index]] = self.IndexedDB[index].get(item[index], [])
                self.IndexedDB[index][item[index]].append(item["cid"])
            else:
                if item["cid"]: self.IndexedDB[index][item["cid"]] = origin_index

    def generate_cid(self) -> int:
        if len(self.IndexedDB["cid"]) == 0:
            return 1
        elif len(self.SpacedCIDList) != 0:
            return min(self.SpacedCIDList)

        return max(self.IndexedDB["cid"].keys()) + 1


    def add_car(self, producer: str, model: str, year: int, price: float) -> bool:
        cid = self.generate_cid()
        car = {
            "cid": cid,
            "producer": producer,
            "model": model,
            "year": correct_year(year),
            "status": "В наличии",
            "price": price,
        }

        self.OriginDB.append(car)
        self.index_item(car, len(self.OriginDB) - 1)

        return True

    def delete_car(self, cid: int) -> bool:
        if cid in self.IndexedDB["cid"].keys():
            self.OriginDB.pop(self.IndexedDB["cid"][cid])
            self.index_db()
            return True
        return False

    def search(self, request, soft_search: bool) -> dict:
        request = str(request)
        request_lower = str.lower(request)
        search_results = {}
        if soft_search:
            for i in range(len(self.OriginDB)):
                for key, value in self.OriginDB[i].items():
                    if request_lower in str.lower(str(value)) or request_lower == str.lower(str(value)):
                        if key not in search_results:
                            search_results[key] = []
                        search_results[key].append(self.OriginDB[i]["cid"])
        else:
            for i in range(len(self.OriginDB)):
                for key, value in self.OriginDB[i].items():
                    if request == str(value):
                        if key not in search_results:
                            search_results[key] = []
                        search_results[key].append(self.OriginDB[i]["cid"])

        return search_results

    def id_list_to_car_list(self, id_list: list) -> list:
        if len(id_list) == 1:
            return [self.OriginDB[self.IndexedDB["cid"][id_list[0]]]]
        return [self.OriginDB[self.IndexedDB["cid"][cid]] for cid in id_list]


class AutoShop:
    def __init__(self, db_path: str = "db.json", bank: float = 0):
        self.db = DB(db_path)
        self.ShopBank = bank
        self.UserBank = 0
        self.GeneralActions = [
            ["Просмотреть все автомобили", self.show_all_cars_ui],
            ["Автомобили в наличии", self.show_cars_in_stock_ui],
            ["Поиск автомобилей", self.search_ui],
        ]
        self.localizer = {
            "auto_list": {
                "cid": "id",
                "producer": "Производитель",
                "model": "Модель",
                "year": "Год выпуска",
                "status": "Статус",
                "price": "Цена",
            },
            "search_results": {
                "cid": "id",
                "producer": "Производителю",
                "model": "Модели",
                "year": "Году выпуска",
                "status": "Статусу",
                "price": "Цене",
            },
        }

    def start(self):
        auto_list_ui(["Добро пожаловать в систему учёта автосалона!"])

        modes = [["Покупатель", self.user_ui], ["Менеджер", self.manager_ui]]
        selector_with_auto_list(modes, "Выберите режим работы")()

    def ask_for_continuation_ui_with_auto_list(self):
        auto_list_ui([["Для выхода введите любой символ", "Для продолжения нажмите Enter"]])
        if input("\n\n> ") != "":
            self.db.export_db()
            sys.exit()

    def manager_ui(self):
        actions = self.GeneralActions
        actions.extend([
            ["Добавить автомобиль", self.add_ui],
            ["Удалить автомобиль", self.delete_ui],
            ["Настроить автомобиль", self.tune_car_ui],
        ])

        while True:
            selector_with_auto_list(actions, "Выберите действие:", top_label = "Режим менеджера", second_top_label = f"Баланс автосалона: {self.ShopBank}₽ || Кол-во автомобилей: {len(self.db.OriginDB)}")()
            self.ask_for_continuation_ui_with_auto_list()

    def user_ui(self):
        actions = self.GeneralActions
        actions.extend([
            ["Купить автомобиль", self.buy_car],
            ["Арендовать автомобиль", self.rent_car],
            ["Вернуть автомобиль", self.back_car],
        ])

        self.UserBank = request_input_with_auto_list("Пожалуйста, введите свой бюджет в рублях", int)
        while True:
            selector_with_auto_list(actions, "Выберите действие:", top_label = "Режим покупателя", second_top_label = f"Ваш баланс: {self.UserBank}₽")()
            self.ask_for_continuation_ui_with_auto_list()

    def show_all_cars_ui(self):
        auto_list_ui(self.db.OriginDB, self.localizer["auto_list"], "Все автомобили", "В автосалоне нет автомобилей!")

    def show_cars_in_stock_ui(self):
        self.check_db()
        cars_in_stock = self.db.IndexedDB["status"]["В наличии"]
        if len(cars_in_stock) == 0:
            auto_list_ui(["Нет доступных автомобилей!"])
            return

        cars_in_stock = self.db.id_list_to_car_list(cars_in_stock)
        auto_list_ui(cars_in_stock, self.localizer["auto_list"], "Автомобили в наличии", "Нет автомобилей в наличии!")

    def search_ui(self):
        self.check_db()
        search_request = request_input_with_auto_list("Введите поисковой запрос", str)
        search_result = self.db.search(search_request, self.db.Settings["Soft search"])

        if len(search_result) == 0:
            auto_list_ui(["Ничего не найдено"])
            return
        elif len(search_result) == 1:
            key = list(search_result.keys())[0]
        else:
            key = selector_with_auto_list([[self.localizer["auto_list"][key], key] for key in search_result.keys()], "Выберите тип совпадений:")

        cars_list = self.db.id_list_to_car_list(search_result[key])
        auto_list_ui(cars_list, self.localizer["auto_list"], f"Найденные автомобили по {str.lower(self.localizer['search_results'][key])}")

    def add_ui(self):
        if (self.db.add_car(request_input_with_auto_list("Введите производителя", str), request_input_with_auto_list("Введите модель", str),
                        request_input_with_auto_list("Введите год выпуска", int), request_input_with_auto_list("Введите стоймость", float))):
            auto_list_ui(["Автомобиль успешно добавлен"])
        else:
            auto_list_ui(["Не удалось добавить автомобиль"])

    def delete_ui(self):
        self.check_db()
        cid = request_input_with_auto_list("Введите id автомобиля, который хотите удалить", int, self.db.IndexedDB["cid"].keys(), error_text = "Нет автомобиля с таким id")
        auto_list_ui(self.db.id_list_to_car_list([cid]), top_label = "Автомобиль, который вы хотите удалить")
        check = selector_with_auto_list([["Да", True], ["Нет", False]], top_label = "Вы точно хотите удалить этот автомобиль?")
        if check:
            self.db.delete_car(cid)
            auto_list_ui(["Автомобиль успешно удалён"])

    def tune_car_ui(self):
        self.check_db()
        cid = request_input_with_auto_list("Введите id автомобиля для настройки: ", int, self.db.IndexedDB["cid"].keys(), error_text = "Нет автомобиля с таким id")
        car_index = self.db.IndexedDB["cid"][cid]
        car = self.db.OriginDB[car_index]
        key = selector_with_auto_list([[self.localizer["auto_list"][key], key] for key in self.localizer["auto_list"].keys() if key != "cid"], "Выберите пункт для изменения")
        new_val = request_input_with_auto_list(f"Старое значение: {car[key]} || Введите новое значение", type(car[key]))

        auto_list_ui([f"Параметр пункт успешно изменён с {self.db.OriginDB[car_index][key]} на {new_val}"])
        self.db.OriginDB[car_index][key] = new_val
        self.db.index_db()

    def check_db(self):
        if len(self.db.IndexedDB) == 0:
            auto_list_ui(["В автосалоне нет автомобилей"])

    def rent_car(self):
        self.check_db()
        cid = request_input_with_auto_list("Введите id автомобиля который хотите арендовать", int, self.db.IndexedDB["cid"].keys(), error_text = "Нет автомобиля с таким id")
        car_index = self.db.IndexedDB["cid"][cid]
        car = self.db.OriginDB[car_index]
        rent_price = round(car["price"] / 30, 2)
        auto_list_ui([car, [f"Стоймость аренды на сутки: {rent_price}", f"Ваш баланс: {self.UserBank}"]], top_label = "Выбранный автомобиль")

        check = selector_with_auto_list([["Да", True], ["Нет", False]], top_label = "Хотите арендовать этот автомобиль?")
        if check:
            if str.lower(car["status"]) == "в наличии":
                if self.UserBank >= rent_price:
                    self.UserBank -= rent_price
                    self.ShopBank += rent_price
                    self.db.OriginDB[car_index]["status"] = "Сдан в аренду"
                    auto_list_ui(["Автомобиль успешно взят в аренду, приятной поездки!"])
                    self.db.index_db()
                else:
                    auto_list_ui(["На вашем счету недостаточно средств!"])
            else:
                auto_list_ui(["Автомобиль уже арендован, попробуйте выбрать другой"])

    def buy_car(self):
        self.check_db()
        cid = request_input_with_auto_list("Введите id автомобиля который хотите купить", int, self.db.IndexedDB["cid"].keys(), error_text = "Нет автомобиля с таким id")
        car_index = self.db.IndexedDB["cid"][cid]
        car = self.db.OriginDB[car_index]
        auto_list_ui([car, f"Ваш баланс: {self.UserBank}"], top_label = "Выбранный автомобиль")
        check = selector_with_auto_list([["Да", True], ["Нет", False]], top_label = "Хотите купить этот автомобиль?")

        if check:
            if str.lower(car["status"]) == "в наличии":
                if self.UserBank >= car["price"]:
                    self.UserBank -= car["price"]
                    self.ShopBank += car["price"]
                    self.db.delete_car(cid)
                    auto_list_ui(["Автомобиль успешно приобретён, обратитесь к любому сотруднику салона, приятной поездки!"])
                    self.db.index_db()
                else:
                    auto_list_ui(["На вашем счету недостаточно средств!"])
            else:
                auto_list_ui(["Автомобиль уже арендован, попробуйте выбрать другой"])

    def back_car(self):
        self.check_db()
        cid = request_input_with_auto_list("Введите id арендованного вами автомобиля", int, self.db.IndexedDB["cid"].keys(), error_text = "Нет автомобиля с таким id")
        car_index = self.db.IndexedDB["cid"][cid]
        car = self.db.OriginDB[car_index]
        auto_list_ui([car], top_label = "Выбранный автомобиль")
        if str.lower(car["status"]) == "сдан в аренду":
            if selector_with_auto_list([["Да", True], ["Нет", False]], top_label = "Хотите вернуть этот автомобиль?"):
                self.db.OriginDB[car_index]["status"] = "В наличии"
                auto_list_ui(["Автомобиль успешно возвращён, спасибо что выбрали нас!"])
        else:
            auto_list_ui(["Данный автомобиль не был сдан в аренду"])


shop = AutoShop()
shop.start()
