#  Задание No3
# 📌 Напишите класс для хранения информации о человеке: 
#     ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год,
#     full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения, 
# но есть возможность получить текущий возраст.

# Вариант решения с методами
class Person_:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self._age = age  # private

    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

    def get_older(self):
        self._age += 1

    def get_age(self) -> int:
        return self._age

# Вариант решения со свойствами
class Person: 
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self._age = age  # private

    @property
    def age(self) -> int:
        return self._age

    @property 
    def full_name(self) -> str:
        return self.firstname + ' ' + self.lastname

    def get_older(self):
        self._age += 1

# Задание No4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
#     ○ шестизначный идентификационный номер
#     ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь



class Employee(Person):
    def __init__(self, firstname: str, lastname: str, age: int, id: int):
        super().__init__(firstname, lastname, age)
        self.id = id
        # self.level = self.calculate_level()

    @property
    def access_level(self) -> int:
        digit_sum = 0

        id_ = self.id
        while id_:
            id_, digit = divmod(id_, 10) # (id_ // 10, id_ % 10)
            digit_sum += digit
        
        return digit_sum % 7

e = Employee('A', "t", 25, 48798)
print(e.full_name)


# import sqlite3


# python_persons = []
# with sqlite3.connect('db.sqlite3') as connection:
#     cursor = connection.cursor()
#     persons = cursor.execute('SELECT * FROM person') # [('surname','name', 15)]

#     for person in persons:
#         python_persons.append(
#             Person_(person[1], person[0], person[2])
