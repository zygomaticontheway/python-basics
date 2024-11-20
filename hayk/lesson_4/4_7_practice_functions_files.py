
def read_file(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()
    return data

def show_file(path):
    text = read_file(path)
    print('-_' *12)
    print(path)
    print('-_' *12)
    print(text)


show_file('result.txt')
show_file('text.txt')
show_file('test1.txt')