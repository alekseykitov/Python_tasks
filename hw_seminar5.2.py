# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, 
# ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь 
# с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

staff = ['Ivan', 'Masha', 'Peter']
salaries = [100, 150, 200]
bonus = ['10.25%', '0.01%','10.00%']

staff_dict =  {e: s * (float(b.removesuffix('%')))/100 for e, s, b in zip(staff, salaries, bonus)} # e = Ivan, s = 100, b = 10.25%

# 'testtexttext'.removesuffix('text') -> 'testtext'
# 'testtexttext'.rstrip('text') -> 'tes'