def largest_digit(n):
    return max(int(digit) for digit in str(n))

num = int(input("Enter a number: "))

print("Largest digit:", largest_digit(num))
