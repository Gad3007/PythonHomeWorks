from datetime import datetime, timedelta


def future_date(days_from_now):
    """Возвращает дату, которая наступит через указанное кол-во дней от текущей даты"""

    # Получение текущей даты и времени
    today = datetime.now()

    # Вычисление даты через указанное колво дней
    future_date = today + timedelta(days=days_from_now)

    # ФОрматирование будущей даты в строку в формате YYYY-MM-DD

    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    days = 30
    print(f'Date {days} days from now: {future_date(days)}')