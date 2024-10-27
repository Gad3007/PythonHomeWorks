# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.

from functools import wraps

from typing import Callable, Any, Optional


def counter(func: Callable) -> Callable:
    """Декоратор для подсчета вызовов функции.
    func: Декорируемая функция
    :return: Обертка функции с подсчетом вызовов.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция-обертка для увеличения и вывода счетчика вызовов функции

        :param args: Позиционные аргументы декорируемой функции
        :param kwargs: Именованные аргументы декорируемой функции
        :return: результат вызова декорируемой функции
        """
        wrapper.count += 1  #Увеличиваем счетчик вызовов на единицу.
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
        return result

    wrapper.count = 0
    return wrapper  # Возвращаем обертку.


@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    """
    Приветствие с возврастом и именем.
    :param name: Имя человека
    :param age: Возвраст человека(по умолчанию None).
    :return: Строка с приветствием.
    """
    if age:
        return "Ого, {name}! Тебе Уже {age} лет, ты быстро растешь".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


@counter
def greeting2(name: str) -> None:
    """
    Приветствие с именем. Вывод
    :param name: Имя человек.
    :return: None.
    """
    print(f'ПРивет, {name}!')


def main() -> None:
    """
    Основная функция для запуска

    :return: None
    """
    greeting("Том")
    greeting("Миша", age=100)
    greeting2("Masha")
    greeting(name="Kata", age=16)


main()
