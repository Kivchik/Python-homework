# С
# помощью
# запросов
# к
# API
# Реализовать
# систему
# в(вывод
# в
# терминал) которая
# будет
# выводить
# информацию
# про
# погоду
params3 = {
    'daily': [
        # Температура
        'temperature_2m_max',  # Максимум за день
        'temperature_2m_min',  # Минимум за день
        'apparent_temperature_max',  # Макс. ощущаемая
        'apparent_temperature_min',  # Мин. ощущаемая

        # Осадки
        'precipitation_sum',  # Сумма осадков
        'precipitation_hours',  # Часы с осадками
        'rain_sum',  # Сумма дождя
        'showers_sum',  # Сумма ливней
        'snowfall_sum',  # Сумма снега

        # Другие параметры
        'weather_code',  # Код погоды (WMO)
        'sunrise',  # Восход
        'sunset',  # Закат
        'sunshine_duration',  # Продолжительность солнца
        'wind_speed_10m_max',  # Макс. скорость ветра
        'wind_gusts_10m_max',  # Макс. порывы
        'wind_direction_10m_dominant',  # Преобладающее направление
        'shortwave_radiation_sum',  # Суммарная радиация
        'uv_index_max',  # Макс. UV индекс
        'et0_fao_evapotranspiration',  # Испаряемость (по FAO)
    ]
}

params2 = {
    'hourly': [
        # Основные показатели
        'european_aqi',  # Индекс качества (европейский)
        'us_aqi',  # Индекс качества (американский)
        'pm10',  # Взвешенные частицы 10 мкм
        'pm2_5',  # Взвешенные частицы 2.5 мкм
        'carbon_monoxide',  # Угарный газ (CO)
        'nitrogen_dioxide',  # Диоксид азота (NO2)
        'sulphur_dioxide',  # Диоксид серы (SO2)
        'ozone',  # Озон (O3)
        'aerosol_optical_depth',  # Аэрозоли
        'dust',  # Пыль
        'ammonia',  # Аммиак (NH3)
    ]
}

# Реализовать ввод широты и долготы с клавиатуры пользователя.Сделать вывод эстетичным и читаемым.

import asyncio

async def auto_list_ui(auto_list: list, supported_parameters: dict = None, top_label: str = None,
                 empty_error_text: str = None, spaces: int = 3, key_val_spacer: str = ": ", min_interface_len: int = 0,
                 second_top_label: str = None):
    if len(auto_list) == 0:
        await auto_list_ui([empty_error_text])
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

async def request_input_with_auto_list(request_text: str, expected_type: type, expected_values: list = None, attempts: int = 999, error_text: str = None, input_marker = "\n\n> "):
    for i in range(attempts):
        await auto_list_ui([request_text])
        user_input = input(input_marker)

        try:
            user_input = expected_type(user_input)
        except ValueError:
            if error_text:
                await auto_list_ui([error_text])
            continue

        if expected_values and user_input in expected_values:
            return user_input
        elif not expected_values:
            return user_input
        else:
            await auto_list_ui([error_text])

    return False

async def request_input(request_text: str, expected_type: type, expected_values: list = None, attempts: int = 999, error_text: str = None):
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

async def selector_with_auto_list(items_list: list, request_text: str = None, pre_item_text: str = "", spacer: str = " - ", post_item_text:str = "", top_label: str = None, second_top_label: str = None):
    request_list = [[]]
    for i in range(len(items_list)):
        request_list[0].append(f"{pre_item_text}{i+1}{spacer}{items_list[i][0]}{post_item_text}")

    await auto_list_ui(request_list, request_text, top_label = top_label, second_top_label = second_top_label)
    user_input = await request_input("\n\n> ", int, range(1, len(items_list) + 1)) - 1
    print(user_input)

    return items_list[user_input][1]


import requests
import datetime
import time

params = {'url': 'https://api.open-meteo.com/v1/forecast', 'params': {
    'latitude': 43.6,
    'longitude': 39.73,
    'current_weather': True,
}}

async def request_weather():
    return requests.get(params["url"], params=params["params"])

in_work = False
response = None
pause_time = 5
async def output():
    last_tick = time.time()
    while True:
        #if not in_work: break

        if last_tick + pause_time < time.time():
            response = await request_weather()
            if response.status_code == 200:
                weather = response.json()['current_weather']
            else:
                continue

            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{now}\nСейчас: {weather['temperature']}C")
            last_tick = time.time()

async def switch_regular_output():
     await output()


async def pass_1():
    print("passed")
    pass

async def main():
    text = [[f"Добро пожаловать в программу отслеживания погоды!"]]
    await  auto_list_ui(text)
    while True:
        action = await selector_with_auto_list([
            ["Посмотреть сводку по погоде за день", pass_1],
            ["Посмотреить сводку по погоде за час", pass_1],
            [f"Переключить отображение текеущей температуры каждые {pause_time} секунд", switch_regular_output],
            [f"Сменить положение", pass_1],
        ],
        top_label=f"Текущее положение: latitude = {params["params"]['latitude']}, longitude = {params["params"]['longitude']}",
        second_top_label="Доступные действия:"
        )
        await action()

if __name__ == "__main__":
    asyncio.run(main())