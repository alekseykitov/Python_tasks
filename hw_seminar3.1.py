# # Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
#  В результирующем списке не должно быть дубликатов. 
# на входе [1,2,3,1,2,1,5,6] , на выходе [1,2]




user_list = [1,2,3,1,2,1,5,6]
num_dict = {}

for i in user_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
result_list = [i for i in num_dict if num_dict[i] > 1]

print(result_list)