num = 12521
flag = 0
lst = []

while(num > 0):
    lst.append(num % 10)
    num = (int)(num/10)

for i in range((int)(len(lst)/2)):
    if lst[i] != lst[len(lst)-1-i]:
        flag = 1

print("Palindrom") if flag == 0 else print("Not a palindrome") 

str1 = "racecar"
str1 = list(str1)
flag = 0
for i in range((int)(len(str1)/2)):
    if str1[i] != str1[len(str1)-1-i]:
        flag = 1

print("Str Palindrome") if flag == 0 else print("Str Not a Palindrome")
    