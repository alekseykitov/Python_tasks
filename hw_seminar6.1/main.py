from problems.eight_queens import check_solution
import random

count = 0
while count < 4:
    queens_positions = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    print(count)
    if check_solution(queens_positions):
        print(queens_positions) 
        count += 1


# print(check_solution([(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]))
