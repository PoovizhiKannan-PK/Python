def findProductExceptSelf(n, arr):
    if n == 0:
        return False
    elif n == 1:
        return arr
    elif n == 2:
        arr[0] = arr[0] + arr[1]
        arr[1] = arr[0] - arr[1]
        arr[0] = arr[0] - arr[1]
        return arr
    else:
        output = []
        for i in range(n):
            product = 1
            for j in range(n):
                if(i != j):
                    product = product * arr[j]
            output.append(product)
        return output


arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    arr.append(int(input()))

print(findProductExceptSelf(n, arr))
