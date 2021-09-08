# For given array of words find the characters that appear in all the words
# LeetCode: "Find Common Characters"


lst = ["bella", "label", "roller"]

output = list(set(lst[0]))

for i in range(1, len(lst)):
    output = list(set(lst[i]) & set(output))
    print(output)

print(output)