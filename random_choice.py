import My_Package.random_from_list
from My_Package.random_from_list import selected_students

studlist = ["Аня", "Маша", "Катя", "Оля", "Света", "Иван", "Петя", "Саша", "Дима", "Максим"]

count = int(input("Введите количество отвечающих: "))

result = selected_students(studlist, count)

print("Сегодня на уроке отвечают:")

for student in result:
    print(student)