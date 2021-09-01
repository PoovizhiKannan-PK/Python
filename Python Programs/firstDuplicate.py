# For an list input of "1,2,3,4,3,2,1", 
# return the "index of original number"(index: 2) and "original number"(num: 3) of first duplicate found
# (first duplicate found is 3(at index 4), not 2(at index 5)). 

def firstDuplicate(arr):
    if arr == [] or n == 1:
        return arr
    else:
        seen = {}
        for i in range(len(arr)):
            if arr[i] in seen.keys():
                return arr[i], seen[arr[i]]
            else:
                seen[arr[i]] = i
        return -1

arr = []

n = int(input("Enter no of inputs"))
for i in range(n):
    arr.append(int(input(str(i)+" th Element: ")))

print(firstDuplicate(arr))