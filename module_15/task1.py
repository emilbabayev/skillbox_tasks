# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.

N = int(input('Введите целое число: '))
odd_numbers = []

for number in range(1, N + 1, 2):
    odd_numbers.append(number)

print(odd_numbers)