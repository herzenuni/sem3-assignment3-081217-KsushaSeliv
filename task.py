

# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?

# Импортируйте необходимые библиотеки

# import 

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 
import pprint

filename = ''

try:

    with open(filename, encoding='utf-8') as data_file:
        
        data = #использовать модуль json и метод для считывания данных: (data_file)

except ________:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


pprint(data)

# Вывести в форматированном виде поля: 

# company, email, phone, address


import pprint 
import json 
filename = 'data.json' 
try: 
with open(filename, encoding='utf-8') as data_file: 
data = json.loads(data_file.read()) 
except OSError: 
print("404. Вы неправильно ввели имя") 
pprint.pprint(data)
