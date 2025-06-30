def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
num = int(input("Enter a number: "))
print("Number of factors:", count_factors(num))
