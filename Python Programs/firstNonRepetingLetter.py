# For input "aaabbbcddeff" find the first non repeating character. output: c


def firstNonRepeatingLetter(arr):
    if arr ==[] or len(arr) == 1:
        return arr
    else:
        tracker = {}
        for i in arr:
            if i in tracker.keys():
                tracker[i] += 1
            else:
                tracker[i] = 1
        for key in tracker:
            if tracker[key] == 1:
                return key  
        return -1


str = input("Enter string: ")
arr = list(str)

print(firstNonRepeatingLetter(arr))