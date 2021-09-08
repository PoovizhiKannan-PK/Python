# For a given lower and upper limit (1,28) print all numbers including limits that are self dividing.
# Example: 128 is self dividing because 128%1 = 0, 128%2 = 0, 128%8 = 0. 1,2,8 are numbers in 128
# And the number must not contain 0 at the end
# LeetCode = "Self Dividing Numbers"

def selfDividing(num):
    if num%10 == 0:
        return False
    else:
        copy = num
        while(num > 0):
            div = num%10
            if copy%div != 0:
                return False
            num = int(num/10)
        return True


lower = 1
upper = 22
output = []

for i in range(lower, upper+1):
    if selfDividing(i):
        output.append(i)

print(output)


