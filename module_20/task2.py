# Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии:
# теперь индексы элементов должны быть простыми числами.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число. Для проверки на простое число напишите отдельную функцию is_prime.
#
# Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return
# и при этом также возвращала список.

def is_prime(num):
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True


def prime_only(data):
    result = list()
    if isinstance(data, dict):
        for i_value, value in enumerate(data.values()):
            if is_prime(i_value):
                result.append(value)
    else:
        for i, value in enumerate(data):
            if is_prime(i):
                result.append(value)

    return result


def main():
    return prime_only('hi world')


print(main())