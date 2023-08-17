# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

import time
from typing import Generator


# 0 1 1 2 3 5 8 13 21 ...
def febonacci() -> Generator[int, None, None]:
    penult = 0
    previous = 1
    yield penult
    yield previous
    while True:
        penult, previous = previous, previous + penult 
        yield previous


x = febonacci()
for _ in range(10):
    print(next(x))