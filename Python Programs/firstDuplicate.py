def firstDuplicate(n, arr):
    if arr == [] or n == 1:
        return arr
    else:
        seen = []
        for i in range(n):
            if arr[i] in seen:
                return arr[i]
            else:
                seen.append(arr[i])
        return -1

arr = []

n = int(input("Enter no of inputs"))
for i in range(n):
    arr.append(int(input(str(i)+" th Element: ")))

print(firstDuplicate(n, arr))