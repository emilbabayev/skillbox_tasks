first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
result = []

for year in range(first_year, second_year + 1):
    temp = year
    while temp != 0:
        counter = 0
        digit = temp % 10
        temp //= 10
        while temp != 0:
            if digit == temp % 10:
                counter += 1
            temp //= 10
        if counter == 2:
            result.append(year)
            break

print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:\n', result)
