# For a given array of integers[1,1,1], find number of subarray sum equals k(2)
# Output = 2. [1,1][1,1]
# This'll work only for positive numbers

def getSum(left, right, lst):
    sum =0
    for i in range(left, right+1):
        sum += lst[i]
    return sum

def sumOfSubArrayEqualsK(lst, k):
    left = 0
    right = 0
    count = 0
    while(left<= right and right < len(lst)):
        sum = getSum(left, right, lst)
        if sum == k:
            count += 1
            right += 1
        elif sum < k:
            right += 1
        else:
             left += 1

    return count


lst = [1,1,1,1]
k = 2

print(sumOfSubArrayEqualsK(lst, k))
