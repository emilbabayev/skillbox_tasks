cards_count = int(input('Введите количество карточек: '))
summ = 0

for card in range(cards_count - 1):
    summ += int(input('Введите номер оставшейся карточки: '))

missing_card = int(cards_count * (cards_count + 1) / 2 - summ)
print(f'Номер пропавшей карточки: {missing_card}')