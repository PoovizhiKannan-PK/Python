# A robot starts from origin (0,0). It moves Up U, Down D, RIght R, Left L. 
# After instruction "UDLR", if it comes back to origin, return true

inst = "UDLRU"
seen = set()
for i in inst:
    if i == "U" and "D" in seen:
        seen.remove("D")
    elif i == "D" and "U" in seen:
        seen.remove("U")
    elif i == "R" and "L" in seen:
        seen.remove("L")
    elif i == "L" and "R" in seen:
        seen.remove("R")
    else:
        seen.add(i)

print("Reached Origin") if seen == {} or seen == set() else print("Roaming somewere")