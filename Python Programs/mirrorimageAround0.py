n = 5
var1 = 1
var2 = 1
# spaces = ' ' *(n-1)

for i in range(n):
    spaces = ' ' * (n-i-1)
    print(spaces, end='')
    for j in range(1, var1+1):
        print(var1-j, end='')
        var1 += 1
    print(spaces)
