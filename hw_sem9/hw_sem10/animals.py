# Задание No5
# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

#  Задание No6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Fish:
    def __init__(self, weight: float)-> None:
        self.weight = weight

    def print_sound(self) -> None:
        print('Bul Bul')

    def print_info(self) -> None:
        print(f'Вес: {self.weight}')


class Bird:
    def __init__(self, weight: float, fly_distance: float)-> None:
        self.weight = weight
        self.fly_distance = fly_distance

    def print_sound(self) -> None:
        print('Chirik')
    
    def print_info(self) -> None:
        print(f'Вес: {self.weight}')
        print(f'Дистанция полета: {self.fly_distance}')


class Dog:
    def __init__(self, weight: float, owner_name: str)-> None:
        self.weight = weight
        self.owner_name = owner_name

    def print_sound(self) -> None:
        print('wouf')

    def print_info(self) -> None:
        print(f'Вес: {self.weight}')
        print(f'Имя хозяина: {self.owner_name}')


fish = Fish(.5)
dog = Dog(20, 'Alexey')
bird = Bird(5, 1500)

print('Fish:')
fish.print_sound()
fish.print_info()

print('Dog:')
dog.print_sound()
dog.print_info()

print('Bird:')
bird.print_sound()
bird.print_info()

animals = [fish, dog, bird]
for animal in animals:
    animal.print_sound()
    animal.print_info()

