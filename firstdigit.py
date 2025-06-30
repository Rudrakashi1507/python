def first_digit(n):
    while n >= 10:
        n //= 10
    return n

num = int(input("Enter a number: "))

print("First digit:", first_digit(num))
