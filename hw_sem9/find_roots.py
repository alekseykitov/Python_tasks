import math

def findind_roots(a: float,b: float,c: float) -> list[float]:
    d = b**2 - 4 * a * c
    if d == 0:
        x = -b / 2 * a
        return [x]
    if d > 0:
        x_1 = (-b + math.sqrt(d)) / 2*a
        x_2 = (-b - math.sqrt(d)) / 2*a
        return [x_1,x_2]   
    return []
 

roots = findind_roots(1, 2, 3)
print(*roots)

# 5000 * 500 = 2500.000
# 5000 * 1 = 5.000