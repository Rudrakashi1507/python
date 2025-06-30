def digits_increasing(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            return False
    return True
num = int(input("Enter a number: "))
if digits_increasing(num):
    print("Yes")
else:
    print("No")
