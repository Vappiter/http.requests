from pprint import pprint
import requests
import json

heroes = ['Hulk', 'Captain America', 'Thanos']

if __name__ == '__main__':
    first_url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
    big_intelligence = 0
    for var1 in range (0,3):
      results = requests.get(first_url + heroes[var1])
      pyt_res = json.loads(results.text)
      intelligence = int(pyt_res['results'][0]['powerstats']['intelligence'] + '\n')
      if big_intelligence < intelligence:
       name_intel  = pyt_res['results'][0]['name'] + ', '   
       big_intelligence = intelligence
    print(f'Самый умный герой {name_intel} его интеллект равен {big_intelligence}')   