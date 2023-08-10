# # В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.
#  За основу возьмите любую статью из википедии или из документации к языку.

text = 'Text for example. Text example with dots. And other for for punctuation symbols!'.lower().split()
print(text)
num_dict = {}
for i in text:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1

print(sorted(num_dict, key=num_dict.get, reverse=True)[:10]) # [key1, key2, ...]