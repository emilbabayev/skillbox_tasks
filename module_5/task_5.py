a = int(input('Число a: '))
b = int(input('Число b: '))
c = int(input('Число c: '))

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)