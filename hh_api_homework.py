import requests
import pprint

url = 'https://api.hh.ru/vacancies'

params = {'text': 'Python', 'area': 1}

result = requests.get(url, params=params).json()

num_of_vac = result['found']

print(num_of_vac)

print(result['items'])

#pprint.pprint(result)
