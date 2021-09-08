# For a given array of integers, one element occurs only once. 
# Find that number
# LeetCode: "Single Number"

lst = [4,2,3,2,4]
seen = {}
for i in lst:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1

for i in seen.keys():
    if seen[i] == 1:
        print(i)
 
 # XOR Method, Xor -> ^

# 0 ^ 8 = 8
# 8 ^ 8 = 0
# so if  value occurs twice, it cancels itself out
# This method works only for even number of duplicates and single unique integer

a = lst[0]
for i in range(1,len(lst)):
    a = a ^ lst[i]
print(a)