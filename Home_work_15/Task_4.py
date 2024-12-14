import argparse


def main():

    # СОздание парсера аргументов

    parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')

    # Добавление обязательных аргументов

    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')

    # Добавление опций
    parser.add_argument('--verbose', action='store_true',help='Вывод дополнительной информации')
    parser.add_argument('--repeat',type=int,default=1,help='Количество повторений строки')

    # Парсинг аргументов

    args = parser.parse_args()

    # Вывод доп информации, если опция вербос установлена

    if args.verbose:
        print(f'Число: {args.number}, Строка: {args.text * args.repeat}')

if __name__ == '__main__':
    main()
