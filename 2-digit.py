def is_special_number(n):
    if 10 <= n <= 99:
        a = n // 10  
        b = n % 10   
        return a * b + a + b == n
    else:
        return False  

num = int(input("Enter a 2-digit number: "))
if is_special_number(num):
    print("True")
else:
    print("False")
