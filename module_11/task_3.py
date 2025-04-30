import math

file_size = float(input('Укажите размер файла для скачивания: '))
internet_speed = float(input('Какова скорость вашего соединения: '))

downloaded = 0
seconds = math.ceil(file_size / internet_speed)
print(seconds)
for sec in range(1, seconds):
    downloaded += internet_speed
    percentage = round(downloaded * 100 / file_size, 2)
    print(f'Прошло {sec} сек. Скачано {round(downloaded, 2)} из {round(file_size, 2)} Мб ({percentage}%)')

print(f'Прошло {seconds} сек. Скачано {round(file_size, 2)} из {round(file_size, 2)} Мб (100%)')
