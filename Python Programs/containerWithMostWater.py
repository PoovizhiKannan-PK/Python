# FOr a given list of non neg integers, each number represent height of a bar in a horizontal bar graph. 
# Find the two bars that has most rectangular area
# This is a LEETCODE problem, search for "Container with most water", to better understand the question


lst = [1,8,6,2,5,4,8,3,7]

start = 0
end = len(lst) -1
maxArea = 0

while(start < end):
    if lst[start] < lst[end] :
        maxArea = max(maxArea, lst[start] * (end-start))
        start += 1
    else:
        maxArea = max(maxArea, lst[end] * (end-start))
        end -= 1

print(maxArea)

