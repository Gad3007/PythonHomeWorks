# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).

text = input("Введите текст: ")

low_text = text.lower()

odd_chars = set()

for symbol in low_text:
    if symbol in odd_chars:
        odd_chars.remove(symbol)
    else:
        odd_chars.add(symbol)

length = len(odd_chars)
if length > 1:
    print("Строка не может быть палиндромом")
else:
    print("Строка является палиндромом")
