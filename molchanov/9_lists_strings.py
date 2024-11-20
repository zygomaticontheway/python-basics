
children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2010', 'Bubnov_2015']

# s_children = sorted(children) # регистр имеет значение при сортировке
# print(s_children)

def by_year(name):
    return name.split('_')[-1] #разделение списка и получение последнего элемента от разделения

s_children = sorted(children, key = by_year)
print(s_children)

# l.append(l1) добавляет список в список - результат = [[1,2,], [w,1,2]]
# l.extened(l1) то же самое что и l+l1 сливает два списка в один - результат = [1,2,,w,1,2]
# s.split() - формирование списка из строки с разделением по пробелам
# s.split('param') - формирование списка из строки по заданному параметру 'param'
# s.join(l) - объединение списка в строку, где s вставится вместо разделителя
# ', '.join(l) - объединит список в строку и вставит ", " как разделитель
# функция sorted с параметрами (переменная, key - ключ по которому сортируется)