import tkinter as tk

# функция для суммы чисел

def my_summ():
    numbers = entry.get().split()
    result = 0
    for number in numbers:
        result += int(number)
    label.config(text=f"Сумма равна: {result}")


root = tk.Tk()
root.title("Сумма чисел")

label = tk.Label(root, text="Введите числа через пробел")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Посчитать сумму", command=my_summ)
button.pack()
root.mainloop()

