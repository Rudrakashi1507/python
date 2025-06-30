def is_harshad(n):
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0
num = int(input("Enter a number: "))
if is_harshad(num):
    print("Yes")
else:
    print("No")
