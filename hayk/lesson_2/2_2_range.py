
# lst = [12, -4, -3, 13, 4, 5, 3, 22, 21, 0, -8]
# print()
# print(lst)
# print(lst.__len__())

# for i in range(len(lst)):
#     if lst[i] < 0:
#         lst[i] = -lst[i]
#     print('step ' + str(lst[i]))
# print(lst[i])

# цикл преобразовать из строк в числа
lst_str = ['2', '3', '4']
for i in range(len(lst_str)):
    lst_str[i] = int(lst_str[i])
    print('step ' + str(lst_str))
print('summary:')
print(lst_str)