import requests
import json

def get_isbn(title, author):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    parameters = {"q": f'intitle:{title} inauthor:{author}', "country": "US"}
    response = requests.get(base_url, params=parameters)
    result = json.loads(response.text)
    items = result['items']
    for item in items:
        print(json.dumps(item, indent=2))
        volume_info = item['volumeInfo']
        if 'industryIdentifiers' in volume_info:
            for identifier in volume_info['industryIdentifiers']:
                if identifier['type'] == 'ISBN_13':
                    return identifier['identifier']
    return None

# title = "Gideon the Ninth"
# author = "Tamsyn Muir"
# isbn = get_isbn(title, author)
# print(f'The ISBN of the book "{title}" by {author} is {isbn}')

from pathlib import Path

fi = Path("d:\\temp\\tweets.json")

with fi.open(encoding='UTF-8') as f:
    data = json.loads(f.read())
    c23 = 0
    for d in data:
        dt = d["tweet"]["created_at"]
        if dt.endswith(" 2023"):
            c23 = c23+1
    print(len(data), c23)