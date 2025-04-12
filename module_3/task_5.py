minutes = int(input('Введите кол-во минут: '))

hours = minutes // 60
remain_minutes = minutes % 60

print(f'В {minutes} минутах - {hours} ч. и {remain_minutes} м.')