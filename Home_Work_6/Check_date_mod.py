




def check_date (date):
    date = list(map(int, date))
    if date[2] % 4 != 0:
        print('Год не високосный')
        if date[1] == (1 or 3 or 5 or 7 or 8 or 10 or 12) or date[1] > 12 or date[2] > 9999:
            if date[0] > 31 or date[2] > 9999 or date[1] > 12:
                return print("Не валидная дата")
            else:
                return print(*date)
        elif date[1] == (4 or 6 or 9 or 11) or date[1] > 12 or date[2] > 9999:
            if date[0] > 30 or date[2] > 9999 or date[1] > 12:
                return print("Не валидная дата")
            else:
                return print(*date)
        elif date[1] == 2:
            if date[0] > 28 or date[2] > 9999 or date[2] > 9999:
                return print("Не валидная дата")
            else:
                return print(*date)
        else:
            return print(*date)
    elif date[2] % 100 == 0:
        if date[2] % 400 == 0:
            # print('Год високосный.')
            _check_leap(date)
        else:
            print('Год не високосный.')
    else:
        print('Год високосный.')
        _check_leap(date)

def _check_leap(date):
    if date[1] == (1 or 3 or 5 or 7 or 8 or 10 or 12) or date[1] > 12 or date[2] > 9999:
        if date[0] > 31 or date[2] > 9999 or date[1] > 12:
            return print("Не валидная дата")
        else:
            return print(*date)
    elif date[1] == (4 or 6 or 9 or 11) or date[1] > 12 or date[2] > 9999:
        if date[0] > 30 or date[2] > 9999 or date[1] > 12:
            return print("Не валидная дата")
        else:
            return print(*date)
    elif date[1] == 2:
        if date[0] > 29 or date[2] > 9999:
            return print("Не валидная дата")
        else:
            return print(*date)
    else:
        return print(*date)


if __name__ == '__main__':
    date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
    check_date(date)
