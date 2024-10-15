import json

import csv


def json_to_csv(json_file, csv_file):
    """Превращает данные из JSON файла в CSV файл."""
    # Чтение данных из JSON файла
    with open(json_file, 'r') as f:
        data = json.load(f)# Загрузка данных из JSON

    # Проверка корректности формата данных

    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):

            raise ValueError("Некоректный формат данных в JSON файле")
    # Запись данных в CSV файл

    with open(csv_file, 'w', newline='') as f:
        fieldnames = data[0].keys()# Получение заголовков из ключей первого словаря
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader() # Запись заголовков
        writer.writerows(data) # Запись данных

if __name__ == "__main__":

    json_to_csv('products.json', 'products.csv')