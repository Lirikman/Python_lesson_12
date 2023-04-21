import requests
import pprint

url = 'https://api.hh.ru/vacancies'

params = {'text': 'NAME:(Python)', 'area': 1}

result = requests.get(url, params=params).json()

# Всего найдено вакансий
total_vac = result['found']
print(f'Всего вакансий по запросу Python: {total_vac}')

# Всего страниц с вакансиями
total_pages = result['pages']
print(f'Всего страниц по запросу Python: {total_pages}')

vac_json = []
for i in range(total_pages):
    vac_json.append(requests.get(url, params={'text': 'NAME:(Python)', 'area': 1, 'page': i, 'per_page': 20}).json())

pprint.pprint(vac_json[30])


#salary = []
#for i in vacancies:
#    salary.append(i['salary'])

#print(salary)
#pprint.pprint(vacancies)
