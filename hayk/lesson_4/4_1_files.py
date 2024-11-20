
f = open('test.txt', 'w', encoding='utf-8')
print (f)
f.write('привет')
f.close()

# same as above
#оператор используется для подключения - сам отключается
# with open('test.txt', 'w', encoding='utf-8') as f:
#     data = f.write('привет Андрей')

with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)