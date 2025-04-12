a, b, c = int(input('a - ')), int(input('b - ')), int(input('c - '))

max_num = a

if b > a:
    max_num = b
if c > max_num:
    max_num = c

print(f'max num - {max_num}')