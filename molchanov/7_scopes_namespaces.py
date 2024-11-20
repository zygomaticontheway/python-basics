
# def a(name):
#     print(locals()) #вывести переменные

# a('Hello')


name = 'Eroha'

def a():
    name = 'Pupkin'
    age = 12
    print('=====1======')
    print(name)
    print('function a NAMESPACE', locals())
    

    def b():
        name = 'PuPkin'
        print('=====4======') #чтение имен идет начиная от локальных, далее смотрит на вложенные, потом поднимается на уровень вверх до глобальных
        print(name)
        print(locals())
    b()
# print('=====2======') # выполнится до вызова функции в глобальном пространстве имен
# print('before NAME~~~~SPACE', locals())

a() # Результат "function a NAMESPACE {'name': 'Pupkin', 'age': 12}""

# print('=====3======') # Результат "... 'name': 'Eroha', 'a': <function a at 0x10c0a7eb0>}" - переменная осталась глобальной, 
#                         #не перезаписалась локальной одноименной переменной которая в функции
# print('after NAME~~~~SPACE', locals())
