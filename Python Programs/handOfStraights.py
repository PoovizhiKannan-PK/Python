# For a given list of numbers, and a target bucker value, see if you can fit the lst of numbers consicutively in the bucker size.
# Lst = [2,4,1,1,3,5] buckets = 3, output = true since [1,1],[2,3],[4,5]
# This is a leetcode problem, check for hand of straights to better understand the problem

lst = [1,2,3,6,2,3,4,7,9] # False, since last set [6,7,9] is not contiguous
w = 3
flag = True


if len(lst)%w != 0:
    flag = False
else:
    for i in range(int(len(lst)/3)):
        minVal = min(lst)
        for j in range(w):
            try:
                lst.remove(minVal)
                minVal = minVal + 1
            except:
                flag = False
                break

print("True") if flag == True else print("False")