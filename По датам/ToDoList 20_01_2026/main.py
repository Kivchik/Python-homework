# Задание: "Умный список дел" (To-Do List App)
# Уровень 1: Базовый (Начальный)
# Создайте простой список задач с возможностью:
# Добавление новой задачи через поле ввода
# Отображение списка задач
# Удаление выбранной задачи
# Минимальный интерфейс:
# Поле Entry для ввода
# Кнопка "Добавить"
# Listbox для отображения задач
# Кнопка "Удалить выбранное"

import tkinter as tk
from tkinter import ttk
import json


def om_start():
    try:
        with open('notes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def on_close(window):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)
    window.destroy()

notes = om_start()


width = 500

main_window = tk.Tk()
main_window.title("ToDo List")
main_window.geometry(f"{width}x500")
main_window.resizable(True, True)
main_window.protocol("WM_DELETE_WINDOW", lambda: on_close(main_window))

label_tittle = ttk.Label(main_window, text="Список задач", font=("Arial", 16))
label_tittle.pack(pady=15)

entry_note = ttk.Entry(main_window, width=50)
entry_note.pack(fill="x")
entry_note.focus_set()

btn_add = ttk.Button(main_window, text="Добавить задачу")
btn_add.pack(pady=10, fill="x")

frame_notes = tk.Frame(main_window, borderwidth=2, relief="sunken")
frame_notes.pack(pady=5, fill="both", expand=True)


def new_note(text=None, add=True, note_id=None):
    if not text:
        text = entry_note.get()

    if text != "":
        if len(notes) == 0:
            note_id = 0
        elif note_id is None:
            note_id = max([int(n_id) for n_id in notes.keys()]) + 1

        frame = tk.Frame(frame_notes, borderwidth=2, relief="sunken")
        frame.pack(pady=5, fill="x")

        entry_note.delete(0, "end")
        note = ttk.Label(frame, text=text, font=("Arial", 10), justify="left", wraplength=width - 55)
        note.grid(row=note_id, column=0, pady=3, padx=2)

        btn_del = ttk.Button(frame, text="Del", width=5)
        btn_del.config(command=lambda: (frame.destroy(), notes.pop(str(note_id))))
        btn_del.grid(row=note_id, column=1, pady=3, padx=2)

        if add:
            notes[note_id] = text


if len(notes) == 0:
    new_note("Это пример заметки, она автоматически подстраивает свой размер в зависимости от длинны текста, так что он не выходит за границы окна")
else:
    for k, v in notes.items():
        new_note(v, add=False, note_id=k)


btn_add.config(command=new_note)

main_window.mainloop()
