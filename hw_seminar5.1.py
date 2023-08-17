# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
#  Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def file_data(absolute_path: str) -> tuple[str, str, str]:
    # /Users/mac/Desktop/GeekBrains/Погружение в Пайтон/hw_seminar5.1.py
    path, file = absolute_path.rsplit('/', maxsplit=1)
    file_name, file_extention = file.rsplit('.', maxsplit=1)
    return path, file_name, file_extention
print(file_data(input('Введите абсолютный путь')))

