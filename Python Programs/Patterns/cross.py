n = int(input("Enter Number: "))


for i in range(1, n+1):
    if i <= n//2:
        s = (" " * (i-1)) + str((n-i+1)) + \
            (" " * ((n-i+1) - i)) + str(i) + " " * (i-1)
        print(s)
    elif i == (n//2)+1:
        s = (" " * (i-1)) + str((n-i+1)) + " " * (i-1)
        print(s)
    else:
        s = (" " * (n-i)) + str((n-i+1)) + \
            (" " * (i-2)) + str(i) + " " * (n-i)
        print(s)
