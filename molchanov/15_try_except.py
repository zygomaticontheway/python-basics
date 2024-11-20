
from re import S


def main():
    d = {'website': 'google', 'url': 'google.ru'}
    try:
        # print(asshole)
        data = d['url']
    except: # если указать KeyError или конкретный тип исключения то будут перехватываться тока эти
        data = 'https://'
        # print('inside except', data)
        # return data
    # finally: #это выполняется всегда до того как сгенерированное исключение будет передано в вызывающий код
    #     print('very important action')
    else: #нужен, чтобы не заграмождать try, в него перейдет исполнение если не встретится исключений
        data = data.upper()
    print(data)

main()
