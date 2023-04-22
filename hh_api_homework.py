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

# Объект для хранения скаченных вакансий с HH.RU по запросу Python
vac_json = []

# Скачиваем вакансии в названии которых содержится слово Python
for i in range(total_pages):
    url = 'https://api.hh.ru/vacancies'
    params = {'text': 'NAME:(Python)', 'area': 1, 'page': i, 'per_page': 20}
    vac_json.append(requests.get(url, params=params).json())

# Анализируем полученную информацию
# Выбираем только те вакансии, в которых указан размер заработной платы в строке 'ОТ'
# Заработную плату считаем по наименьшей, то есть той что в строке 'ОТ'
all_salary = 0
all_vac = 0
for i in vac_json:
    items = i['items']
    count_vac = 0
    summ_salary = 0
    for j in items:
        if j['salary'] is not None:
            s = j['salary']
            if s['from'] is not None:
                count_vac += 1
                summ_salary += s['from']
    all_salary += summ_salary
    all_vac += count_vac

# Рассчитываем средний уровень заработной платы
average_salary = all_salary//all_vac
print(f'Средняя заработная плата по запросу Python в Москве: {average_salary} руб.')


#Cчетчик = 11