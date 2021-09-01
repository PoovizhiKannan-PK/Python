# Anagrams
str1 = "asdf"
str2 = "fdsade"

print(set(str1) == set(str2))

# Remove Duplicates
str3 = "asssdddfdrergvnfhnhggf"

print(list(set(str3)))

# Fibonacci
n = 5
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a+b
