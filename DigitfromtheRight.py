def nth_digit_from_right(num, n):
    return (num // (10 ** (n - 1))) % 10
number = int(input("Enter a number: "))
n = int(input("Enter the position from the right: "))
print("Output:", nth_digit_from_right(number, n))
