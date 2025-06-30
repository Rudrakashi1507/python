def count_even_odd_digits(n):
    even_count = 0
    odd_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

num = int(input("Enter a number: "))

even, odd = count_even_odd_digits(num)
print(f"Even: {even}, Odd: {odd}")
