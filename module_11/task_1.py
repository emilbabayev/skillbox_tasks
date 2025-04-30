euro_price = float(input('Стоимость покупки в евро: '))

dollar_price = euro_price * 1.25
ruble_price = dollar_price * 60.87

print(f'Стоимость покупки в рублях: {ruble_price}')

