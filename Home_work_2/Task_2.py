num = int(input("Введите десятичное число: "))
he_num = []
i = 0


if num == 0:
    he_num.append('0')
if num < 0:
    num = abs(num)
    i = 1



while num:
    dNA = num % 16
    if dNA > 9 and dNA < 16:
        if dNA == 10:
            he_num.append('A')
        elif dNA == 11:
            he_num.append('B')
        elif dNA == 12:
            he_num.append('C')
        elif dNA == 13:
            he_num.append('D')
        elif dNA == 14:
            he_num.append('E')
        elif dNA == 15:
            he_num.append('F')
    else:
        he_num.append(num % 16)
    num = num // 16
he_num.append("oX")
if i == 1:
    he_num.append('-')
he_num.reverse()
print(*he_num,sep='')
