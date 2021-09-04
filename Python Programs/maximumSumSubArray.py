# For a given list of numbers[-1, 2, 3, -4], find the contiguous sub array with maximum sum
# Here max sum is 5 [2,3], if we add the whole array, its 0

lst = [1, 5, 2, -4, 6]

maxSum = lst[0]
currentSum = maxSum
for i in range(1, len(lst)):
    currentSum = max(lst[i], (lst[i]+currentSum))
    maxSum = max(currentSum, maxSum)

print(maxSum)