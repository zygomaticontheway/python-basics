
# a = False

# if 2 * 2 == 4:
#     print('Ok')
# else:
#     print('ne ok')


# pwd = '123'
# user_input = '00000'

# if 'u' in 'pupkin':
#     print('welcome')
# else:
#     print('wrong')

# s = '1234578'

# if len(s) == 8:
#     print ('Length 8')
# elif len(s) == 6:
#     print ('Length 6')
# else:
#     print('no 6 or 8')

# pwd = '123'
# user_input = ''

# # if user_input:
# #     if user_input == pwd:
# #         print('welcome')
# #     else:
# #         print('wrong')
# # else:
# #     print('input smth pls')

# print('welcome') if user_input else print('wrong')

# задание вывести
# 1 - 100
# 3 - Fizz
# 5 - Buzz
# 3 & 5 - FizzBuzz
# i

def fizz_buzz (i):
    if not (i % 5) and not (i % 3):
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(7)
fizz_buzz(10)
fizz_buzz(15)
fizz_buzz(17)