
# 1000 : 15 = mass : x

# x = 15 * mass / 1000
ingredients = {
    'salt': 15,
    'pepper': 5
}
# same as below
# def get_sault_mass(m):
#     return m * 15 /1000
# def get_pepper_mass(m):
#     return m * 5 /1000

def get_ingredient_mass(m, ingr):
    # return m * ingredients[ingr] / 1000
    return m * ingredients.get(ingr, 0) / 1000


# print(get_sault_mass (1500))
print(get_ingredient_mass(1500, 'salt'))

# обертка вокруг print - параметр file означает
# куда будет выводиться принт, можно записывать в файл
# print автоматом вставляет перенос каретки как \n 
def print_wrapper(text):
    with open('files/readme_1.txt', 'a') as f:
        print(text, file = f)

print_wrapper(1)
print_wrapper(2)
print_wrapper('mazafaka')