# file = open('files/readme.txt')
# # file.write('2')
# data = file.read()
# print(data)
# file.close()
 
folder_path = 'files/'
pic_name = 'meme.png' 
pic = folder_path + pic_name
file = open(pic, 'rb')

#  file = open(pic)

new_file = open(folder_path + 'copy_' + pic_name, 'wb')
# print(new_file)

new_file.write(file.read())

# контекстный менеджер with ... as
with open(folder_path + 'readme.txt', 'w') as file_1:
    file_1.write('Goodbue Yerevan')