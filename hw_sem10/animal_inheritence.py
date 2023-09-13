from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, weight: float) -> None:
        self.weight = weight
    
    @abstractmethod
    def print_info(self) -> None:
        pass

    @abstractmethod
    def print_sound(self) -> None:
        pass


class Fish(Animal):
    def __init__(self, weight: float)-> None:
        super().__init__(weight)

    def print_sound(self) -> None:
        print('Bul Bul')

    def print_info(self) -> None:
        print(f'Вес: {self.weight}')


class Bird(Animal):
    def __init__(self, weight: float, fly_distance: float)-> None:
        super().__init__(weight)
        self.fly_distance = fly_distance

    def print_sound(self) -> None:
        print('Chirik')
    
    def print_info(self) -> None:
        print(f'Вес: {self.weight}')
        print(f'Дистанция полета: {self.fly_distance}')


class Dog(Animal):
    def __init__(self, weight: float, owner_name: str)-> None:
        super().__init__(weight)
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

animals: list[Animal] = [dog, bird]
for animal in animals:
    animal.print_sound()
    animal.print_info()


def print_info_about_animal(animal: Animal):
    print(animal.)
