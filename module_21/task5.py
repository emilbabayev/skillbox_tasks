def calculating_math_func(data, calculated=dict()):
    if data in calculated.keys():
        return calculated[data]

    result = 1
    for index in range(1, data + 1):
        result *= index

    result /= data ** 3
    result = result ** 10
    calculated[data] = result
    return result


print(calculating_math_func(5))
print(calculating_math_func(5))
print(calculating_math_func(10))
print(calculating_math_func(10))
print(calculating_math_func(10))
print(calculating_math_func(20))
print(calculating_math_func(30))
print(calculating_math_func(5))
print(calculating_math_func(30))

