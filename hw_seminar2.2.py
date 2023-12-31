#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.

# 7 # base 10 (0, 1, 2, ..., 9)
# 4

# 111 # base 2 (7)
# 100 # base 2 (4)

# # base 2
# 100 4
# 101 5
# 110 6
# 111 7
# 1000 8
# 1001 9
# 1010 10
# 1011

# # base 16
# # 0, 1, 2, 3, 9, a (10), b (11), c (12), d (13), e (14), f (15)

# # 15 -> f
# # 16 -> 10

# # 135 (base 2)
# 135 | 2 (1)
#  67 | 2 (1)
#  33 | 2 (1)
#  16 | 2 (0)
#   8 | 2 (0)
#   4 | 2 (0)
#   2 | 2 (0)
#   1 | 2 (1)

# 135 -> 10000111

# # 135 (base 16)
# 135 | 16 (7)
#   8 | 16 (8)
#   0 | 16 (0)

# 135 -> 87

# ... + 8 * 16^1 + 7 * 16^0

def to_hex(num: int) -> str:
    alphabet = '0123456789abcdef'
    result = ''
    while num != 0:
        index = num % 16
        num //= 16
        result = alphabet[index] + result
    return result

user_num = int(input('Введите целое неотрицательное число: '))

print(to_hex(user_num))

print((hex(user_num)[2:]))
