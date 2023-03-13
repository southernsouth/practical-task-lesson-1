import requests, json

city = input('Місто: ')

url = 'https://api.yelp.com/v3/businesses/search?location=%s&term=restaurants&categories=&sort_by=best_match' % (city)

headers = {
    "accept": "application/json",
    "Authorization": "Bearer 7mN2tjnjHKvfURu58xciRcTbZnXZ8KapeZaPTkYijqsFR9LiF1h81Ccx31iY2C6-IAB2iQpPnhP3_t84FGXsPqojbjGhNGQ6cOu7iHYNc1yQBMJyPlsHgT4EnisPZHYx"
}

data = requests.get(url, headers=headers).json()

try:
    data = data['businesses']
    text = ''
    for item in data:
        text += '--- %s ---' % (item['name'])
        text += '\nРейтинг: ' + str(item['rating'])
        text += '\nКількість переглядів: ' + str(item['review_count'])
        categories = item['categories']
        for i in range(len(categories)):
            categories[i] = categories[i]['title']
        text += '\nКатегорії: ' + ', '.join(categories)
        text += '\nАдреса: ' + item['location']['address1']
        text += '\n' + item['url']
        text += '\n\n'
    print(text)
except: print('Немає результатів')
