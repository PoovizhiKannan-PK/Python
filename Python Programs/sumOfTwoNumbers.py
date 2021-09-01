# For a givin sorted list, find the indices of two numbers in that list whose value add up to the target value

lst = [2,7,11,15]
target = 22
seen = {}

for i in range(len(lst)):
    if lst[i] > target:
        break
    if lst[i] in seen.keys():
        print([seen[lst[i]], i])
        break
    else:
        seen[target-lst[i]] = i
