# for  given two lists, find two numbers, one from each list, whose sum add up to the target value

def sumOfTwo(arr1, arr2, sum):
    seen = set()
    for i in arr1:
        seen.add(sum-i)
    for i in arr2:
        if i in seen:
            return True
    return False



arr1 = []
arr2 = []

n1 = int(input("number of items in arr1"))
n2 = int(input("number of items in arr2"))

for i in range(n1):
    arr1.append(int(input("Elements in arr1: ")))

for i in range(n2):
    arr2.append(int(input("Elements in arr2: ")))

sum = int(input("Enter the sum to be: ")) 
print(sumOfTwo(arr1, arr2, sum))