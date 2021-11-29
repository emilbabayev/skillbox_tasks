def gen_numbers(n):
    if n == 0:
        print(0)
    else:
        gen_numbers(n-1)
        print(n)


stop_num = int(input('До какого числа выводить? '))
gen_numbers(stop_num)