def sum_to_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

num = int(input("Enter a number: "))
result = sum_to_single_digit(num)
print("Output:", result)