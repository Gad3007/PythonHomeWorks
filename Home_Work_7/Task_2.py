import os
import zipfile
from pathlib import Path
import os.path


# def zipdir(path, ziph):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))
#
# if __name__ == '__main__':
#     zipf = zipfile.ZipFile('Python.zip', 'w',zipfile.ZIP_DEFLATED)
#     zipdir('Home_Work_7/', zipf)
#     zipf.close()

def zip_directory(source_dir, output_zip):
    """
    Создает архив .zip из указанного каталога.
    :param source_dir: Путь к исходному каталогу для архивирования.
    :param output_zip: Путь к целевому архиву .zip.
    """
    # Создаем объект ZipFile для записи архива

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # проходим по всем файлам и папкам в исходном каталоге
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Полный путь к текущему каталогу
                file_path = os.path.join(root, file)
                # Добавляем файл в архив с путем относительно исходного каталога
                zipf.write(file_path, os.path.relpath(file_path, source_dir))

zip_directory('E:/PyProjects/PythonHomeWorks/Home_Work_7', 'E:/PyProjects/PythonHomeWorks/Home_Work_7/output.zip')