# The input array [-4, 1-, 2, 5, 8] is sorted in accending order
# Give output of array of squared elements in accending order

def memoryEfficientSortedSquaredArray(n, arr):
    if arr == [] or n == 1:
        return arr;
    else:
        for i in range(n):
            arr[i] = arr[i] * arr[i]
        arr.sort()
        return arr

def timeEfficientSortedSquaredArray(n, arr):
    if arr == [] or n == 1:
        return arr
    else:
        outarr = [0] * n
        i = 0
        j = n-1

        for k in range(n):
            if(abs(arr[i]) > abs(arr[j])):
                outarr[n-k-1] = arr[i] * arr[i]
                i += 1
            else:
                outarr[n-k-1] = arr[j] * arr[j]
                j -= 1
        return outarr

arr = []
n = int(input("Enter no of items"))
for i in range(n):
    arr.append(int(input(str(i)+" th Element: ")))


print(memoryEfficientSortedSquaredArray(n, arr))
print(timeEfficientSortedSquaredArray(n, arr))