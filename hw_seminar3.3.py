# Задача 1 HARD 
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 10) многочлена и записать как многочлен степени k.
#  Пример:

#  k=2  - это максимальная степень многочлена, то есть в данном случае будет x2
#  - > 2*x² + 4*x + 5 = 0  при списке [2 ,4 ,5 ]
#        или  x² + 5 = 0   при списке [1 ,0 ,5 ]
#        или  10*x² = 0   при списке [10 ,0 ,0 ]
# k=3 - > 5*x^3 + 6*x^2 + 7*x + 10 = 0 при списке [ 5 , 6 , 7, 10]


from random import randint


def get_random_coefs(k: int) -> list[int]:
    return [randint(0, 10) for _ in range(k)]


def get_part(coef: int, power: int) -> str:
    if coef == 0:
        return ''
    
    if coef == 1:
        coef_str = ''
    else:
        coef_str = f'{coef}*'
    
    if power == 1:
        return f'{coef_str}x'
    if power == 0:
        return str(coef)
    return f'{coef_str}x^{power}'


def get_mnogochlen(coefs: list[int]) -> str:
    k = len(coefs)
    powers = reversed(range(0, k))
    parts = [get_part(c, p) for c, p in zip(coefs, powers)]
    return ' + '.join(p for p in parts if p) + ' = 0'


k = int(input('Enter k: '))
coefs = get_random_coefs(k)
print(coefs)
print(get_mnogochlen(coefs))