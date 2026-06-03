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
        print(f"Имя - {self.name}, порода - {self.kind}, возраст - {self.age}, вес - {self.weight}")

    def newweight(self):
        print(f"Имя - {self.name}, вес после обеда - {self.weight}")

dog1 = Dog("Шарик", "дворняга", 4, 10)
dog2 = Dog("Рэкс", "овчарка", 5, 15)

dog1.info()
dog2.info()

dog1.eat("кость")
dog2.eat("мясо")

dog1.newweight()
dog2.newweight()