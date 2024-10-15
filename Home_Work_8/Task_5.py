import csv


import json


def convert_csv_to_json(input_file, output_file):
    books_by_author = {} # Словарь для хранения книг по авторам

    # Чтение данных из CSV файла

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            author = row['author']
            book = {
                'название': row['name'],
                'год издания': row['year']

            }
            if author in books_by_author:
                books_by_author[author].append(book) #Добавляем книгу к сушествующему автору
            else:
                books_by_author[author] = [book] # Создаем новый список для нового автора
    with open(output_file, 'w',encoding='utf-8') as f:
        json.dump(books_by_author, f,indent=4,ensure_ascii=False) # Сохраняем данные в ДСОН формате


if __name__ == '__main__':
    convert_csv_to_json('books.csv', 'books_by_author.json')
