# Triangle
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()

#reverse * triangle

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

# Number triangle
for i in range(n):
    for j in range(i+1):
        print(j+1, end='')
    print()

# Mountain
print('Mountain')
for i in range(n*2):
    if i < n:
        for j in range(i+1):
            print(j+1, end='')
        print()
    else:
        for j in range((n*2)-i):
            print(j+1, end='')
        print()

# Mountain with peak
print('Mountain with peak:')
for i in range((n*2)-1):
    if i < n:
        for j in range(i+1):
            print(j+1, end='')
        print()
    else:
        for j in range((n*2)-i-1):
            print(j+1, end='')
        print()

# Pointy Triangle
print('Pointy Triangle')
for i in range(n):
    spaces = ' '*(int((n-i+1)/2))
    print(spaces, end='')
    for j in range(i+1):
        print(j+1, ' ', end='')
    print(spaces)
