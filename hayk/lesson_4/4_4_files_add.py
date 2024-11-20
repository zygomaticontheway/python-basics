
text = 'asdasdasd'
files = ['test.txt', 'test1.txt', 'test3.txt']

for file_name in files:
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write('привет \n')
# print(data)