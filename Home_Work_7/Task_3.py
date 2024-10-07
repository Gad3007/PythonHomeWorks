import os

import time


def delete_old_files(directory, days_old):
    """
    Удаляет файлы в указанном каталоге, которые не изменялись более
    заданного количества дней.
    :param directory: Путь к каталогу, в котором нужно удалить
    старые файлы.
    :param days_old: Количество дней, после которых файлы считаются
    старыми.
    """

    now = time.time() # Текушее время в секундах с начала эпохи
    cutoff = now - (days_old * 86400) # Преобразуем количество дгнй в секунды(86400 секунд в дне)

    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file) # Полный путь к файлу
            file_mod_time = os.path.getmtime(file_path) # Время последнего использования
            # Если время последнего изменения меньше порогового значения, удаляем файл
            if file_mod_time < cutoff:
                os.remove(file_path) # Удаляем файл
                print(f'Удален файл: {file_path}')


delete_old_files('E:/PyProjects/PythonHomeWorks/Home_Work_7', 30)