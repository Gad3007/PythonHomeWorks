import fractions


from fractions import Fraction

num_1 = input("Введите первое число через /: ").split("/")
num_2 = input("Введите второе число через /: ").split("/")

int_num_1 = map(int,num_1)
int_num_2 = map(int,num_2)

drob_1 = Fraction(*int_num_1)
drob_2 = Fraction(*int_num_2)


pro = drob_1 * drob_2
summa = drob_1 + drob_2

print("Произведение дробей: ", pro)
print("Сумма дробей: ", summa)







