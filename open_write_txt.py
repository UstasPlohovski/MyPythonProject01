text = input("Введите текст: ")

with open("user_data.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Текст успешно записан в файл user_data.txt")