import requests

headers = {
    'X-Naver-Client-Id': '4DgH_eHrrKIpV5SkJxuL',
    'X-Naver-Client-Secret': 'WU9ri3ByPW',
}

params = {
    'query': '동대문맛집',
    'display': '10',
    'start': '1',
    'sort': 'sim',
}

response = requests.get('https://openapi.naver.com/v1/search/blog.json', headers=headers, params=params)
data = response.json()
for i in range(0,3):
    print(data['items'][i])