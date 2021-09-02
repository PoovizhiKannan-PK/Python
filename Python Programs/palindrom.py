# Check if Palindrome
# Number

num = 12521   # Just convert it to a string
flag = 0
lst = []

while(num > 0):
    lst.append(num % 10)
    num = (int)(num/10)

for i in range((int)(len(lst)/2)):
    if lst[i] != lst[len(lst)-1-i]:
        flag = 1

print("Palindrom") if flag == 0 else print("Not a palindrome") 

# Normal String
str1 = "racecar"
flag = 0
for i in range((int)(len(str1)/2)):
    if str1[i] != str1[len(str1)-1-i]:
        flag = 1

print("Str Palindrome") if flag == 0 else print("Str Not a Palindrome")
    
# Sentence ignoring space and other characters and case

sent = "A man, a plan, a canal: Panama"
output = ""
flag == 0
for i in sent:
    if i.isalpha():
        output += i

output = output.lower()

for i in range((int)(len(output)/2)):
    if output[i] != output[len(output) -i -1]:
        flag = 1
        break

print("Not a palindrome") if flag == 1 else print("Palindrome")
