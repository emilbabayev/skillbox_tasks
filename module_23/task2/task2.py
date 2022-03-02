import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    result = 0
    try:
        result = round(x / y, 4)
        return result
    except ZeroDivisionError:
        raise


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    result = 0
    try:
        result = round(y / x, 4)
        return result
    except ZeroDivisionError:
        raise


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])

        result_data = list()
        for num in my_list:
            result_data.append(str(num))

        with open('result.txt', 'a') as result_file:
            result_file.write(' '.join(result_data))
            result_file.write('\n')