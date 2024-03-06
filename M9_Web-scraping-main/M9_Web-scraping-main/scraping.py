import json
import requests
from bs4 import BeautifulSoup

# Функція для отримання даних зі сторінки сайту
def get_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Функція для отримання цитат зі сторінки
def extract_quotes(page_data):
    quotes = []
    for quote in page_data.select('div.quote'):
        text = quote.select_one('span.text').text
        author = quote.select_one('small.author').text
        tags = [tag.text for tag in quote.select('a.tag')]
        quotes.append({
            'quote': text,
            'author': author,
            'tags': tags
        })
    return quotes

# Функція для отримання посилання на наступну сторінку
def get_next_page_url(page_data, base_url):
    next_page = page_data.select_one('li.next > a')
    if next_page:
        return f"{base_url}{next_page['href']}"
    return None


# Головна функція для скрапінгу та створення файлів
def scrape_quotes():
    base_url = 'http://quotes.toscrape.com'
    quotes_data = []

    # Парсимо першу сторінку та отримуємо всі цитати
    current_url = base_url
    while current_url:
        page_data = get_page_data(current_url)
        quotes_data.extend(extract_quotes(page_data))
        current_url = get_next_page_url(page_data, base_url)  # Оновлено: передавати base_url

    # Зберігаємо отримані дані у файл quotes.json
    with open('quotes.json', 'w', encoding='utf-8') as quotes_file:
        json.dump(quotes_data, quotes_file, ensure_ascii=False, indent=4)

    # Отримуємо список унікальних авторів зі збережених цитат
    unique_authors = list(set(quote['author'] for quote in quotes_data))
    authors_data = []
    for author in unique_authors:
        authors_data.append({
            'fullname': author,
            'born_date': '',
            'born_location': '',
            'description': ''
        })

    # Зберігаємо дані про авторів у файл authors.json
    with open('authors.json', 'w', encoding='utf-8') as authors_file:
        json.dump(authors_data, authors_file, ensure_ascii=False, indent=4)

    print("Дані успішно зібрані та збережені у файли quotes.json та authors.json.")

# Викликаємо головну функцію для скрапінгу та створення файлів
scrape_quotes()

