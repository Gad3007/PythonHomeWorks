import os

def find_files_by_extension(directory, extension):
    """
    Находит и перечисляет все файлы с заданным расширением в
    указанном каталоге и всех его подкаталогах.
    :param directory: Путь к каталогу, в котором нужно искать файлы.
    :param extension: Расширение файлов для поиска (например,
    '.txt').
    """
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, заканчивается ли имя файла на заданное расширение
            if file.endswith(extension):
                # Формируем полный путь к файлу и выводим его
                print(os.path.join(root, file))


find_files_by_extension('E:/PyProjects/PythonHomeWorks/Home_Work_7', '.py')