# import config #импортирует весь файл
# при импорте также происходит выполнение кода файла
# from config import * #так копируется только переменная из файла
#from config import token #так копируются все объекты из импортируемого модуля в текущее пространство имен

print(locals())
print()
print('~~~~~~~~~~~~~')

from config import token

print(locals())

# token = 'hello world' #заново переопределяется импортированная переменная
# print(locals())

# # print(dir(email)) #посмотреть атрибуты, свойства, методы

# print(email) #для вызова переменной (свойства содержащегося в файле) нужно вызывать через имя.свойство
