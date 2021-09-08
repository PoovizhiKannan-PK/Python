# Given array of 2n integers, make n pairs such that sum of min of each par is max
# [2,1,4,3] --> min(1,2)+min(4,3) --> 4

lst = [2,1,4,3]
lst.sort()
sum = 0
for i in range(0,len(lst),2):
    sum += min(lst[i], lst[i+1])

print(sum)