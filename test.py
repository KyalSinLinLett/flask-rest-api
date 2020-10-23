import requests

BASE = 'http://127.0.0.1:5000/'

data = [
	{'likes': 23, 'name': 'qwerty', 'views': 1200}, 
	{'likes': 33, 'name': 'qwerty1', 'views': 12400}, 
	{'likes': 324, 'name': 'qwerty2', 'views': 122300}, 
	{'likes': 22, 'name': 'qwerty3', 'views': 511200}
]

# for i in range(len(data)):
# 	response = requests.put(BASE + 'video/' + str(i), data[i])
# 	print(response.json())

# response = requests.delete(BASE + 'video/0')
# print(response)

response = requests.patch(BASE + 'video/2', {'likes': 23, 'views': 12643})
print(response.json())
# input()

# response = requests.get(BASE + 'video/2')
# print(response.json())