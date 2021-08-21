
def sortedSquaredArray(n, arr):
    if arr == [] or n == 1:
        return arr;
    else:
        for i in range(n):
            arr[i] = arr[i] * arr[i]
        arr.sort()
        return arr


arr = []
n = int(input("Enter no of items"))
for i in range(n):
    arr.append(int(input(str(i)+" th Element: ")))

print(sortedSquaredArray(n, arr))