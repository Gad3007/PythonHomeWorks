# Задача 3. Число наоборот
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225
# Подсказка № 1
# Функция reversal(x) должна обрабатывать каждую цифру числа, начиная с
# последней и добавляя её в новое число. Преобразование можно сделать, используя
# остаток от деления и целочисленное деление.
# Подсказка № 2
# В функции reversal(x) переменная count отслеживает количество цифр, а
# revers_x хранит перевёрнутое число. Не забудьте обновлять revers_x на каждой
# итерации.
# Подсказка № 3
# После ввода чисел и их переворачивания с помощью функции reversal, сложите
# перевёрнутые числа. Затем примените reversal к результату суммы, чтобы получить
# окончательный результат.

num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))
def reversal(x):

    revers_x = 0
    while True:
        revers_x = revers_x * 10
        revers_x = revers_x + x % 10
        x //= 10

        if x <= 0:

            return revers_x


print(f'Первое число наоборот: {reversal(num_one)}')
print(f'Второе число наоборот: {reversal(num_two)}')
sum = reversal(num_one) + reversal(num_two)
print(f'Cумма чисел: {reversal(num_one) + reversal(num_two)}')
print(f'Cумма наоборот: {reversal(sum)}')