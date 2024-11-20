# создать user.txt
# записать туда имя и фамилию
# данные получать из терминала

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')

with open('user.txt', 'w', encoding='utf-8') as f:
    f.write(user_name + ' ' + user_surname)