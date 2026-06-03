class Dog:
    def __init__(self, name, kind, age, weight):
        self.name = name
        self.kind = kind
        self.age = age
        self.weight = weight

    def sleep(self):
        print(f"{self.name} спит...")

    def eat(self, food):
        print(f"{self.name} кушает {food}")
        self.weight += 0.5

    def info(self):
        print(
            f"Имя - {self.name}, "
            f"порода - {self.kind}, "
            f"возраст - {self.age}, "
            f"вес - {self.weight}"
        )


dogs = []

# Ввод количества собак
while True:
    try:
        count = int(input("Сколько у вас собак: "))

        if count <= 0:
            raise ValueError

        break

    except ValueError:
        print("Ошибка: количество собак должно быть положительным целым числом.\n")


# Создание объектов Dog
for i in range(count):

    print(f"\nВвод данных для собаки №{i + 1}")

    # Ввод имени
    while True:
        try:
            name = input("Введите имя собаки: ")

            if name.isdigit():
                raise ValueError

            if name.strip() == "":
                raise ValueError

            break

        except ValueError:
            print("Ошибка: имя не может быть числом или пустой строкой.")

    # Ввод породы
    while True:
        try:
            kind = input("Введите породу собаки: ")

            if kind.isdigit():
                raise ValueError

            if kind.strip() == "":
                raise ValueError

            break

        except ValueError:
            print("Ошибка: порода не может быть числом или пустой строкой.")

    # Ввод возраста
    while True:
        try:
            age = int(input("Введите возраст собаки: "))

            if age <= 0:
                raise ValueError

            break

        except ValueError:
            print("Ошибка: возраст должен быть положительным целым числом.")

    # Ввод веса
    while True:
        try:
            weight = int(input("Введите вес собаки: "))

            if weight <= 0:
                raise ValueError

            break

        except ValueError:
            print("Ошибка: вес должен быть положительным целым числом.")

    # Создание объекта
    dog = Dog(name, kind, age, weight)

    # Добавление в список
    dogs.append(dog)


# Вывод информации о всех собаках
print("\nИнформация о собаках:")

for dog in dogs:
    dog.info()