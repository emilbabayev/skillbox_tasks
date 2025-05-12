acceptable_danger = float(input('Введите максимально допустимый уровень опасности: '))

# D = x ** 3 - 3 * x ** 2 - 12 * x + 10

min_depth = 0
max_depth = 4
danger = 0
counter = 0

while True:
    current_depth = (min_depth + max_depth) / 2
    danger = current_depth ** 3 - 3 * current_depth ** 2 - 12 * current_depth + 10

    if danger > 0:
        min_depth = current_depth
    else:
        max_depth = current_depth

    if abs(danger) < acceptable_danger:
        break

print(f'Приблизительная глубина безопасной кладки: {current_depth}')