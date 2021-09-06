# Given an array of integers [2,3,4,5], return an array of containing all even inters followed by 
# odd integers


lst = [1,2,6,5,3,4]

start = 0
end = len(lst)-1

for i in range(int(len(lst)/2)):
    while(lst[start] %2 == 0):
        start += 1
    while(lst[end]%2 == 1):
        end -= 1
    if(start < end):
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

print(lst)