def my_zip(iterable1, iterable2):
    if len(iterable1) < len(iterable2):
        for i_el, el in enumerate(iterable1):
            yield el, iterable2[i_el]
    else:
        for i_el, el in enumerate(iterable2):
            yield iterable1[i_el], el


text = 'hello'
numbers = (10, 20, 30, 40, 50, 60)

for value1, value2 in my_zip(text, numbers):
    print('({}, {})'.format(value1, value2))