import requests
import pprint

url = 'https://api.hh.ru/vacancies'

params = {'text': 'NAME:(Python-разработчик)', 'area': 1}

result = requests.get(url, params=params).json()

total_vac = result['found']
#print(f'Всего вакансий по запросу Python: {total_vac}')

total_pages = result['pages']
#print(f'Всего страниц по запросу Python: {total_pages}')

vac_json = []

# Поиск вакансий в названии которых содержится "Python-разработчик" на HH.RU в Москве
for i in range(total_pages):
    url = 'https://api.hh.ru/vacancies'
    params = {'text': 'NAME:(Python-разработчик)', 'area': 1, 'page': i, 'per_page': 20}
    vac_json.append(requests.get(url, params=params).json())

all_skills = []
actual_skills = ['Python', 'Django', 'Flask', 'MongoDB', 'FastAPI', 'SQL', 'MySQL', 'PostgreSQL', 'React', 'Git',
                 'HTTP', 'Linux', 'Docker']

# Поиск основных навыков (actual_skills) в найденных вакансиях
for i in vac_json:
    items = i['items']
    for j in items:
        if j['snippet'] is not None:
            s = j['snippet']
            if s['requirement'] is not None:
                for h in actual_skills:
                    if h in s['requirement']:
                        all_skills.append(s['requirement'])
                        break

dict_skills = {'Python': 0, 'Django': 0, 'Flask': 0, 'MongoDB': 0, 'FastAPI': 0, 'SQL': 0, 'MySQL': 0, 'PostgreSQL': 0,
               'React': 0, 'Git': 0,
               'HTTP': 0, 'Linux': 0, 'Docker': 0}

# Подсчёт найденных навыков
for i in actual_skills:
    for j in all_skills:
        if i in j:
            dict_skills[i] += 1

# Сортировка словаря навыков
sorted_skills_keys = sorted(dict_skills, key=dict_skills.get)
sorted_dict_skills = {}

for i in sorted_skills_keys:
    sorted_dict_skills[i] = dict_skills[i]

#print(sorted_dict_skills)

# Считаем сумму всех значений навыков
sum_per = 0
for i in sorted_dict_skills:
    sum_per += sorted_dict_skills.get(i)

# Вычисляем процент каждого навыка
dict_skills_per = {}
for i in sorted_dict_skills:
    dict_skills_per[i] = round((sorted_dict_skills.get(i) * 100) / 815, 2)

# Выводим информацию ТОП-10 необходимых навыков Python-разработчика
skills_percent = [f'{key} - {value}%' for key, value in dict_skills_per.items()]
skills_percent.reverse()
print('ТОП-10 навыков Python-разработчика')
for i in range(10):
    print(skills_percent[i])