summ_salary = 0
for month in range(12):
    salary = int(input('Введите зарплату сотрудника: '))
    summ_salary += salary

average_salary = summ_salary / 12
print(f'Средняя зарплата за год: {average_salary}')