import tkinter as tk

# функция для ввода данных, записи их в файл и вывод их в итоговое сообщение
def save_and_write():
    # Получаем данные из полей ввода
    first_name = entry_name.get()
    last_name = entry_lastname.get()

    # Записываем данные в файл
    with open("myfirstappinfo.txt", "w", encoding="utf-8") as file:
        file.write(first_name + "\n")
        file.write(last_name)

    # Читаем данные из файла
    with open("myfirstappinfo.txt", "r", encoding="utf-8") as file:
        first_name = file.readline().strip()
        last_name = file.readline().strip()

    # Выводим приветствие
    label_result.config(text=f"Привет, {first_name} {last_name}!")


# Создание окна
root = tk.Tk()
root.title("Моя первая программа")
root.geometry("350x200")

# Метка и поле для имени
label_name = tk.Label(root, text="Введите имя:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

# Метка и поле для фамилии
label_lastname = tk.Label(root, text="Введите фамилию:")
label_lastname.pack()

entry_lastname = tk.Entry(root)
entry_lastname.pack()

# Кнопка сохранения
button = tk.Button(
    root,
    text="Сохранить данные.",
    command=save_and_write
)
# button.pack(pady=10)
button.pack()

# Метка для результата
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()