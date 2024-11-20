
# визуализация и пошаговое выполнение скрипта https://pythontutor.com/render.html

#___список___

lst = [12, -4, -3, 13, 4, 5, 3, 22, 21, 0, -8]
print()
print(lst)

# print(lst[3]) #вывод элемента с индексом 3, т.е. четвертый по счету

# lst [4] = 99
# print(lst)

# ___ЦИКЛ___
sum_elem = 0 #для суммирования элементов списка
sum_elem_ = 0
max_elem = lst[0]
min_elem = lst[0]

for elem in lst:
    if max_elem <= elem:
        # sum_elem = sum_elem + elem
        max_elem = elem
        print('max step element = ' + str(max_elem))
    elif min_elem >= elem:
        min_elem = elem
        print('min step element = ' + str(min_elem))
    # else:
    #     # sum_elem_ = sum_elem_ + elem
    #     sum_elem_ -= elem
print('resume:')
print('max element = ' + str(max_elem))
print('min element = ' + str(min_elem))

# print('сумма положительных: ' + str(sum_elem))
# print('сумма отрицательных: ' + str(sum_elem_))
