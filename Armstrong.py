def is_armstrong_number(n):
    if 100 <= n <= 999:
        digits = [int(d) for d in str(n)]
        sum_of_cubes = sum(d ** 3 for d in digits)
        return sum_of_cubes == n
    else:
        return False  

num = int(input("Enter a 3-digit number: "))

if is_armstrong_number(num):
    print("Armstrong")
else:
    print("Not Armstrong")

