# For a given sorted array, do binary Search

lst = [1,2,3,4,5,6,7,8,9]
target = 8
left = 0
right = len(lst)-1

while(left < right):
    mid = int(left + (right-left)/2)
    if lst[mid] == target:
        print("Found at ", mid+1)
        break
    elif target > lst[mid]:
        left = mid +1
    else:
        right = mid-1
