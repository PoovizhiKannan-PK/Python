def duplicateWithMinimalIndex(n, arr):
    if arr==[] or n == 1:
        return arr
    else:
        seen = {}
        minIndex = -1
        for i in range(n):
            if arr[i] in seen.values():
                if (i < minIndex or minIndex == -1):
                    minIndex = i       
            else:
                seen[i] = arr[i]
        if minIndex == -1:
            return minIndex
        return arr[minIndex]

arr = []

n = int(input("Enter Number of Elements: "))
for i in range(n):
    arr.append(int(input()))

print("Duplicate with Minimum Index: ",duplicateWithMinimalIndex(n, arr))
