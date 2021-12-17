n = 4
spaceCount = n
count = 0
for i in range(n):
    spaces = ' ' * spaceCount
    print(spaces, end="")
    for j in range(n):
        if i % 2 == 0:
            print(count+1, end=' ')
            count += 1
        else:
            print(count*2 - j - i, end=' ')
            count += 1
    print('')
    spaceCount -= 1
