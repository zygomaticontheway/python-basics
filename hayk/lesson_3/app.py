# user = ['Гайк', 'Инанц', 29, 176]

# print(user[0])
# print(user[1])

# user = {
# 	"name": "Гайк",
# 	"lastname": "Инанц",
# 	"age": 29,
# 	"height": 178
# }


# for key, value in user.items():
# 	print(key + ' => ' + str(value))

# for value in user.values():
# 	print(value)

# for key in user:
# 	print(key + ' => ' + str(user[key]))


# user = {}
# user["name"] =  "Гайк"
# user["lastname"] =  "Инанц"
# user["age"] =  29
# user["height"] =  178

# print(user['name'])
# print(user['lastname'])

# user['name'] = 'Анатолий'
# user['gender'] = 'M'
# print(user)



users = [
	{
		"id": 1,
		"name": 'Анатолий',
		"age": 27
	},
	{
		"id": 2,
		"name": 'Максим',
		"age": 32
	},
	{
		"id": 3,
		"name": 'Ольга',
		"age": 28
	},
	{
		"id": 4,
		"name": 'Степан',
		"age": 35
	}
]

# for user in users:
# 	if user['age'] < 30:
# 		print(user['name'])

sum_ = 0

for user in users:
	sum_ += user['age']

print(sum_)


