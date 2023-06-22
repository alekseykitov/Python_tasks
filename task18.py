# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

list_size = int(input('Введите количество элементов в списке: '))
user_list = []

for i in range(list_size):
    num = int(input(f'Введите {i+1} элемент: '))
    user_list.append(num)
print(user_list)
user_num = int(input('Введите число, которое нужно найти в списке: '))
close_num = 0
difference = user_num
for i in user_list:
    if i == user_num:
        close_num = i
        break
    else:
        if abs(i - user_num) < difference:
            close_num = i
print(f'Самое близкое к искомому числу - {close_num}')
