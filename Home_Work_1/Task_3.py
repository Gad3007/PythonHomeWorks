# Задача 3. Простые числа
# Напишите программу, которая считает количество простых чисел в заданной
# последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. Последовательность
# задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
# итерация — одно число.
# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.
# Количество простых чисел в последовательности: 4.
# Подсказка № 1
# Чтобы определить, является ли число простым, создайте вложенный цикл. Внешний
# цикл будет проходить по всем числам из последовательности, а внутренний цикл будет
# проверять, делится ли текущее число на любые числа от 2 до его квадратного корня.
# Если число делится, оно не простое, и вы можете выйти из внутреннего цикла.
# Подсказка № 2
# Инициализируйте переменную для подсчёта количества простых чисел. Внутри
# внешнего цикла, если текущее число оказалось простым, увеличьте значение этой
# переменной на 1.
# Подсказка № 3
# Вложенный цикл должен проверять делимость числа от 2 до числа, меньшего
# текущего числа. Если число делится на любое значение, кроме 1 и самого себя, то оно
# не является простым.

numbers_in = int(input("Введите кол-во чисел: "))
count = 0

for i in range(numbers_in):
    user_num = int(input("Введите число: "))
    if user_num > 1:
        for j in range(2,user_num):
            if user_num % j == 0:
                break
        else:
            count+=1
print("Кол-во простых чисел: " , count)



