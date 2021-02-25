num = 5678346756
sum = 0

while(num != 0):
    rem = num%10
    sum += rem
    num = (int)(num/10)
    if num == 0:
        if (int)(sum/10) == 0:
            num = 0
        else:
            num = sum
            sum = 0

print(sum)