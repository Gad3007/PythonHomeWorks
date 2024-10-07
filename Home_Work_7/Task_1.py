import os


def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
    """
    Переименовывает файлы в указанном каталоге.


    :param directory: Путь к каталогу с файлами.
    :param final_name: Конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param old_extension: Расширение исходного файла.
    :param new_extension: Расширение конечного файла.
    :param name_range: Диапозон сохраняемого оригинального имени (начало, конец).

    """


    # Проверяем существование каталога

    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")

    # Получаем список файлов с указанным расширением

    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]

    if not files:
        print("Файлы с указанным расширением не найдены")
        return

    # Определяем формат номера с ведущими нулями

    format_string = f"{{:0{num_digits}d}}"

    # Перебираем файлы и переименовываем их

    for index, file_name in enumerate(files, start=1):

        # Извлекаем базовое имя файла без расширения

        base_name = os.path.splitext(file_name)[0]

        # Извлекаем часть имени файла по заданному диапозону

        if name_range:

            start, end = name_range
            extracted_name = base_name[start-1:end] # Индексы диапозона начинаются с 0
        else:
            extracted_name = base_name

        # Формируем новое имя файла

        new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"

        # Полные пути для старого и нового файла

        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)

        # Переименование файла

        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{file_name}' в '{new_file_name}'")


# Пример использования функции

if __name__ == "__main__":
    # import sys
    # # Проверяем количество аргументов командной строки
    # if len(sys.argv) != 6:
    #     print("Usage: python file_rename.py <directory><final_name><num_digits><old_extension><new_extension>")
    #     sys.exit(1)
    #
    # directory = sys.argv[1]
    # final_name = sys.argv[2]
    # num_digits = int(sys.argv[3])
    # old_extension = sys.argv[4]
    # new_extension = sys.argv[5]

    # Например диапазон [3, 6]

    name_range = [3, 6]

    batch_rename_files('E:/PyProjects/PythonHomeWorks/Home_Work_7','Task' , 3, '.py', '.py', name_range)