import os

import json

import glob

def merge_json_files(input_files, output_file):
    """Объединяет данные из нескольких JSON файлов в один."""
    merge_data = [] # Список для хранения объединенных данных
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f) # Чтение данных из файла
                merge_data.extend(data) # Добавление данных в общий список
        except json.JSONDecodeError:
            print(f"Ошибка чтения JSON файла: {file}")
    with open(output_file,'w') as f:
        json.dump(merge_data, f, indent=4) # Сохранение объединенных данных в новый файл


if __name__ == '__main__':
    # Получаем все JSON файлы в текущей директории
    json_files = glob.glob('employees*.json')
    merge_json_files(json_files, 'all_employees.json')





