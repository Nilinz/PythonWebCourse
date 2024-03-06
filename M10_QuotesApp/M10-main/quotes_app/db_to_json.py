import pymongo
import json
from config import get_mongo_uri
from bson import ObjectId 

def export_data_to_json():
    # Отримання URI для MongoDB з конфігураційного файлу
    mongo_uri = get_mongo_uri()

    # Підключення до MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client.get_database()

    # Отримання даних з колекції authors
    authors_data = list(db.authors.find({}))
    
    # Перетворення ObjectId у рядок для кожного запису в authors_data
    for author in authors_data:
        author['_id'] = str(author['_id'])

    # Збереження даних з колекції authors у файл JSON
    with open('authors.json', 'w', encoding='utf-8') as json_file:
        json.dump(authors_data, json_file, ensure_ascii=False, indent=4)

    print('Дані з колекції authors були експортовані у файл authors.json')

    # Отримання даних з колекції quotes
    quotes_data = list(db.quotes.find({}))

    # Перетворення ObjectId у рядок для кожного запису в quotes_data
    for quote in quotes_data:
        quote['_id'] = str(quote['_id'])

    # Збереження даних з колекції quotes у файл JSON
    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes_data, json_file, ensure_ascii=False, indent=4)

    print('Дані з колекції quotes були експортовані у файл quotes.json')

if __name__ == '__main__':
    export_data_to_json()
