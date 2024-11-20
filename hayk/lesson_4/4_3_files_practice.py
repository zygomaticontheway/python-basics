# считать содержимое test.txt
# преобразовать данные в числа
# посчитать сумму

with open('/Users/zygomactic/Study_Py/test.txt', 'r', encoding='utf-8') as file:
    lst = file.read().split(',')
print(lst)

sum = 0
for i in lst:
    sum += int(i)
print(sum)