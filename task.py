import pprint
import json

filename = 'data.json'

try:
    with open(filename, encoding='utf-8') as data_file:
        json_file = open('data.json', 'r')
        fl = json_file.read()
        data = json.loads(fl)
except FileExistsError:
    print("Файл не найден!")

pprint.pprint(data)

# Вывести в форматированном виде поля: company, email, phone, address

for i in enumerate(data):
	dict = {}
	dict.update(
		{'company':i.get('company'),
		 'email':i.get('email'),
		 'phone':i.get('phone'),
		 'address':i.get('address')})

	pprint.pprint(dict)
