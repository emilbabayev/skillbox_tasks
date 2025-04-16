a = int(input('Начало отрезка: '))
b = int(input('Конец отрезка: '))
summ = 0
counter = 0

print('Числа из отрезка, которые делятся на 3:')
for number in range(a, b + 1):
    if number % 3 == 0:
        print(number)
        summ += number
        counter += 1

result = summ / counter
if int(result) == result:
    result = int(result)

print(f'Среднее арифметическое этих чисел: {result}')
