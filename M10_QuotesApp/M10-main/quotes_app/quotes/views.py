import os
import json
from django.shortcuts import render, redirect
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from .models import Quote, Tag, Author

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_data_from_json(file_name):
    file_path = os.path.join(BASE_DIR, file_name)
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def main(request):
    quotes_data = read_data_from_json('quotes.json')
    return render(request, 'quotes/index.html', {'quotes': quotes_data})

def authors(request):
    authors_data = read_data_from_json('authors.json')
    return render(request, 'quotes/authors.html', {'authors': authors_data})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            # Зберігаємо дані форми в новий словник
            new_author_data = {
                "fullname": form.cleaned_data["fullname"],
                "born_date": form.cleaned_data["born_date"],
                "born_location": form.cleaned_data["born_location"],
                "description": form.cleaned_data["description"]
            }

            # Зчитуємо дані з існуючого файлу authors.json
            authors_data = read_data_from_json('authors.json')

            # Додаємо нового автора до списку авторів
            authors_data.append(new_author_data)

            # Зберігаємо оновлені дані у файл authors.json
            with open(os.path.join(BASE_DIR, 'authors.json'), 'w', encoding='utf-8') as json_file:
                json.dump(authors_data, json_file, ensure_ascii=False, indent=4)

            return redirect(to='quotes:main')
    else:
        form = AuthorForm()

    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data["tags"].split(',')
            author_name = form.cleaned_data["author"]
            quote_text = form.cleaned_data["quote"]

            
            author, created = Author.objects.get_or_create(fullname=author_name)

            
            quote = Quote.objects.create(quote=quote_text, author=author)
            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name.strip())
                quote.tags.add(tag)

            # Отримайте поточні дані з quotes.json
            quotes_data = read_data_from_json('quotes.json')

            # Додайте нову цитату до списку цитат
            new_quote_data = {
                "_id": str(quote.id),  # ID цитати в базі даних Django
                "tags": tags,
                "author": author_name,
                "quote": quote_text
            }
            quotes_data.append(new_quote_data)

            # Збережіть оновлені дані у quotes.json
            with open(os.path.join(BASE_DIR, 'quotes.json'), 'w', encoding='utf-8') as json_file:
                json.dump(quotes_data, json_file, ensure_ascii=False, indent=4)

            return redirect('quotes:main')
    else:
        form = QuoteForm()

    return render(request, 'quotes/add_quote.html', {'form': form})

