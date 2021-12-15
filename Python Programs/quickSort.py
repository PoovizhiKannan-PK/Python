
def partition(arr, start, end):
    # You are storing the pivot index because after sorting left and right elements, you have swap pivot with end
    pivot_index = start
    pivot = arr[pivot_index]

    while(start < end):
        while(start < len(arr) and arr[start] <= pivot):
            start += 1
        while(arr[end] > pivot):
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end


def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        partition(arr, start, pi-1)
        partition(arr, pi+1, end)


arr = [11, 9, 29, 7, 2, 15, 28]
quick_sort(arr, 0, len(arr)-1)

print(arr)
