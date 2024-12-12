import random

# Константа для достижения просветления

NIRVANA_KARMA = 500

# Определение пользовательских исключений


class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. следует сократить порции.")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние-грех!")


# Функция, моделирующая один день жизни

def one_day():

    # Случайное кол-во кармы от 1 до 7

    day_karma = random.randint(1, 7)

    if random.randint(1, 10) == 5:

        # Случайный выбор исключений

        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma



def main():
    karma = 0

    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                # Прибавляем карму за один день

                karma += one_day()
            except Exception as ex:
                # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')

            # Проверяем, достигнуто ли необходимое количество кармы
            if karma >= NIRVANA_KARMA:
                break

    print('Вы достигли Нирваны!')
    print('Omm')



if __name__ == "__main__":
    main()



