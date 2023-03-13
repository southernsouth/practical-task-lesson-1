import requests, json

def get_text(sort_data):
    if len(sort_data) != 0:
        text = ''
        for i in sort_data:
            text += '--- %s ---' % (i['volumeInfo']['title'])
            try: text += '\nАвтори: ' + ', '.join(i['volumeInfo']['authors'])
            except: ...
            try: text += '\nДата публікації: ' + i['volumeInfo']['publishedDate']
            except: ...
            try: text += '\nОпис: ' + i['volumeInfo']['description']
            except: ...
            try: text += '\nКількість сторінок: ' + str(i['volumeInfo']['pageCount'])
            except: ...
            try: text += '\nКатегорії: ' + ', '.join(i['volumeInfo']['categories'])
            except: ...
            text += '\n\n'
            return text
    else: return 'Немає результатів'

def get_by_name():
    name = input('Назва: ')
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=%s+intitle:keyes&key=AIzaSyBE-wVgVmGOvgsbLkETRPNc8yWgAiYDhnk' % (name)).json()
    sort_data = []

    if data['totalItems'] != 0:
        for item in data['items']:
            if name in item['volumeInfo']['title']:
                sort_data.append(item)

    text = get_text(sort_data)
    print(text)

def get_by_author():
    author = input('Автор: ')
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=%s+inauthor:keyes&key=AIzaSyBE-wVgVmGOvgsbLkETRPNc8yWgAiYDhnk' % (author)).json()
    sort_data = []

    if data['totalItems'] != 0:
        for item in data['items']:
            try:
                item['volumeInfo']['authors']
                check = False
                for a in item['volumeInfo']['authors']:
                    if author in a:
                        check = True
                if check:
                    sort_data.append(item)
            except: ...

    text = get_text(sort_data)
    print(text)

method = input('Знайти по назві - 1, знайти по автору - 2\n')
if method == '1': get_by_name()
elif method == '2': get_by_author()
