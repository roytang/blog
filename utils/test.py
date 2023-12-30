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

title = "Gideon the Ninth"
author = "Tamsyn Muir"
isbn = get_isbn(title, author)
print(f'The ISBN of the book "{title}" by {author} is {isbn}')
