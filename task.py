import pprint 
import json 
filename = 'data.json' 
try: 
 with open(filename, encoding='utf-8') as data_file: 
  data = json.loads(data_file.read()) 
except OSError: 
 print('Вы неправильно ввели имя файла ') 
pprint.pprint(data)
