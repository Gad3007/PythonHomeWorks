my_list = [1, 1, 3, 2, 2, 1, 4, 5, 6, 7, 7, 2]

new_list = []
print(f'{my_list} - Исходный список ')

for i in my_list:
    if my_list.count(i) > 1 and i not in new_list:
        new_list.append(i)

print(f'{ new_list} - Cписок дублирующихся элементов')


for j in new_list:
    if new_list.count(j) > 1:
        new_list.remove(j)
my_set = set(new_list)
my_set = list(my_set)
print(f'{my_set} - Результирующий список ')