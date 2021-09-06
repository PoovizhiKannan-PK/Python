# For a given array [0,1,2,0] return the peak index  i.e., 2
# This is a leet Code problem - "Peak Index In A Mountain Array"

# lst = [0,1,2,0]
lst = [0,1,1,0]
peak = 0
isAPeak = False
for i in range(1, len(lst)-1):
    if lst[i] > lst[peak]:
        peak = i
        if lst[i-1] < lst[i] > lst[i+1]:
            isAPeak = True

print(peak) if isAPeak == True else print("No Peaks")