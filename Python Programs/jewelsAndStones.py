# For a given string1 = "aaaBBAA", find the number of characters in string2 = "aA" is present in string 1
# Here the answer is 5, since a(string 2) occurs 3 times and A(string 2) occurs 2 times in String1. So 3 + 2 = 5
# This is a leetcode problem, check for "Jewels and Stones" to better understand the problem

j = "aAbc"
s = "aAAbbb"
jewels = 0

for i in range(len(s)):
    if s[i] in j:
        jewels += 1

print(jewels)

