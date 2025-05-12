start_amp = float(input('Введите начальную амплитуду: '))
finish_amp = float(input('Введите амплитуду остановки: '))

counts = 0

while start_amp > finish_amp:
    start_amp *= 0.9
    counts += 1

print(f'Маятник считается остановившимся через {counts} колебаний')