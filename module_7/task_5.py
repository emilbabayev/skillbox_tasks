for num in range(10, 100):
    first_digit = num // 10
    second_digit = num % 10
    if (first_digit * second_digit * 3) == num:
        print(num)