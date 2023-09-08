import csv
import hw_sem8.generation_csv_file as generation_csv_file
from hw_sem8.find_roots import findind_roots
from typing import Callable, Generator


def get_row_from_csv(file: str) -> list:
    with open(file, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row
    return 0

# def find_roots_from_csv(row: str) -> list[float]:
#     with open()


rows = get_row_from_csv('Random_Numbers.csv')
for row in rows:
    numbers = [int(e) for e in row]
    roots = findind_roots(*numbers)
    print('{}x^2 + {}x + {} = {}'.format(*numbers, roots))
