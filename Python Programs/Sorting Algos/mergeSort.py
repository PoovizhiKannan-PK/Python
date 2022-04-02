class MergeSort:
    def __init__(self, array):
        self.array = array
        self.array = MergeSort.sort(self.array)

    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            # splitting the array
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]

            # recussion
            MergeSort.sort(left)
            MergeSort.sort(right)

            # sorting array
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < (len(right)):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return array


array = [3, 7, 5, 8, 10, 99, 2, 556, 23, 72]
# sort(array)
ms = MergeSort(array)
# ms.sort(array)
print(ms.array)
