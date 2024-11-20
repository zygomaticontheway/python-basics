# из файла text.txt переписать построчно названия товаров в файл result.txt

with open('/Users/zygomactic/Study_Py/text.txt', 'r', encoding='utf-8') as file:
    lst = file.read().split(',')
print(lst)

with open('/Users/zygomactic/Study_Py/result.txt', 'w', encoding='utf-8') as file:
    file.write('')


with open('result.txt', 'a', encoding='utf-8') as f:
    # for i in lst:
    #     f.write(i + '\n')
    f.write('\n'.join(lst)) #этот лайфхак убирает перенос строки \n в конце

