# Reverse array with no extra space

lst = ["a", "b","c", "d", "e"]

for i in range((int)(len(lst)/2)):
    lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i] 

print(lst)

str1 = "Hello"

str1 = str1[-1::-1] # [Start:end:step]

print(str1)

