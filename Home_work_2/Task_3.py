roman_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
arab_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

number = int(input("Введите число: "))

while number > 0:
    for item in arab_numbers:
        while item <= number:
                number = number - item
                print(roman_numbers[arab_numbers.index(item)],end='')









