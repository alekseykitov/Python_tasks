import csv
import json
import pickle
import os


# os.stat(filepath).st_size # bytes

# 1. Размер каждого файла (можем получить от ОС)
# 2. Размер каждой папки (можем только посчитать)
# 3. У каждой папки или файла должен быть указан предок
# 4. У каждого файла или папки должен быть собственный путь

# recursion('/')
# /users/alexey/file.txt
# Добавляем размер файла к папкам:
#   /users/alexey + size(file.txt)
#   /users + size(file.txt)
#   / + size(file.txt)


TYPE_DIRECTORY = 'directory'
TYPE_FILE = 'file'

# x = {
#     'entry_path': {
#         'size': 0,
#         'type': TYPE_DIRECTORY | TYPE_FILE,
#         'parent': './../' # os.path.dirname(entry_path)
#     }
# }


def __get_entries_info_recoursively(directory: str, data: dict) -> None:
    # entries = os.listdir(directory)
    # files = [e for e in entries if os.path.isfile(os.path.join(directory, e))]
    root, directories, file_names = next(os.walk(directory)) # возвращает путь, название папок, имя файлов)

    for file in file_names:
        file_path = os.path.join(root, file) # путь к текущему файлу
        file_size = os.stat(file_path).st_size # размер текущего файла
        data[file_path] = {'size': file_size, 'type': TYPE_FILE, 'parent': directory} # сохроняем данные в словарь data
        
        file_path = data[file_path]['parent']
        while file_path in data:
            data[file_path]['size'] += file_size
            file_path = data[file_path]['parent']
        # /users/alexey/file.txt
        
    # pprint((root, directories, file_names))
    for sub_directory in directories:
        # print('Это папка')
        directory_path = os.path.join(root, sub_directory)
        data[directory_path] = {'size': 0, 'type': TYPE_DIRECTORY, 'parent': directory}
        
        __get_entries_info_recoursively(os.path.join(root, sub_directory), data)

# 
def get_entries_info_recoursively(directory: str) -> dict:
    data = dict()
    data[directory] = {'size': 0, 'type': TYPE_DIRECTORY, 'parent': ''}
    __get_entries_info_recoursively(directory, data)
    return data



def save_entries_info_as_json(entries: dict, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)


def save_entries_info_as_csv(entries: dict, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, ['path', 'type', 'size', 'parent'])
        writer.writeheader()
        for entry_path, entry_info in entries.items():
            writer.writerow({
                'path': entry_path,
                **entry_info,
            })

def save_entries_info_as_pickle(entries: dict, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(entries, f)
