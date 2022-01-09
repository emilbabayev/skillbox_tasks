def my_sum(data):
    result = 0
    for sub in data:
        if isinstance(sub, int):
            result += sub
        else:
            result += my_sum(sub)

    return result


numbers = [[1, 2, [3]], [1], 3, [5, 6, [9, 2], 1], [5, 10], [13], [1, 3]]
print(my_sum(numbers))

numbers2 = (1, 2, 5, 8, 12, 9)
print(my_sum(numbers2))
