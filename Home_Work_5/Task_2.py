names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]



def calc_bonus(names, salary, bonus):
    bonus = [i.strip('%') for i in bonus]
    bonus = [float(i) for i in bonus]
    sum_pr = [(num1*num2)/ 100 for num1, num2 in zip(salary,bonus)]

    result = {names: sum_pr for names, sum_pr in zip(names, sum_pr)}
    print(f'Cотрудники и их премия с учётом процента: {result}')

calc_bonus(names,salary,bonus)


