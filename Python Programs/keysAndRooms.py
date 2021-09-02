# There are bunch of rooms and each room contains some key.
# You can access room 0 directly and get keys from it
# After that, for a room i, you can access it only if you already have the key for that room
# Return true if you can access all the keys


# lst = [[1,3], [3,0,1], [2], [0]] # Invalid, you cannot access room 2, because, room 0 and 1 did not have the key for room 2
lst = [[1], [2], [3], []]
flag = 0

roomKeys = set()
for i in lst[0]:
    roomKeys.add(i)

for i in range(1, len(lst)):
    if i in roomKeys:
        for j in lst[i]:
            roomKeys.add(j)
    else:
        flag = 1
        break

print("Valid") if flag == 0 else print("InValid")