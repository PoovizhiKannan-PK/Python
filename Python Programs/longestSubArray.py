# FOr a given list of number [1,2,3,4,5] and a sum 9, find the loggest sub array whose sum of values is equal to the sum given.
# Ans is arr[2,4][(leftbound of the sub array), (right bound of the sub array)] not arr[4,5]


def longestSubArray(lst, total):
    print(lst, total)
    start = 0
    end = 0
    finalSum = 0
    finalStart, finalEnd = [ 0, 0]
    while end < len(lst):
        finalSum += lst[end]
        end += 1
        while(start < end and finalSum > total):
            finalSum -= lst[start]
            start += 1
        if (finalSum == total and end-start > finalEnd-finalStart):
            finalEnd = end
            finalStart = start
    return [finalStart+1, finalEnd]

# n = int(input("number of elements in the array list"))
n =5
# lst = [1,2,3,4,5,0,0,0,7,8,9,10]
lst = [1,2,3,5,7]
# for i in range(n):
#     lst.append(int(input()))

# total = int(input("ENter the sum: "))
total = 12
print(longestSubArray(lst, total))