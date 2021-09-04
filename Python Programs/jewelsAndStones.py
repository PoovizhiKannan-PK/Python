# For a given string1 = "aaaBBAA", find the number of characters in string2 = "aA" is present in string 1
# Here the answer is 5, since a(string 2) occurs 3 times and A(string 2) occurs 2 times in String1. So 3 + 2 = 5
# This is a leetcode problem, check for "Jewels and Stones" to better understand the problem

j = "B"
s = "aAAbbb"
stones = {}
for i in s:
    if i in stones.keys():
        stones[i] += 1
    else:
        stones[i] = 1

jewels = 0

for i in j:
    if i in stones.keys():
        jewels += stones[i]

print(jewels)

