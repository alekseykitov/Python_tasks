# Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
1
user_num = input('Введите трехзначное число ')
count = 0
summ = 0

for i in range(len(user_num)):
    count += 1
if count == 3:
    for i in range(len(user_num)):
        summ += int(user_num[i])
    print(summ)
else:
    print('Ошибка! Введите трехзначне число!')

