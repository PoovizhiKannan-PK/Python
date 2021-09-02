# For a given input string "ab#c", find the output string "ac".
# Here # means backspace, thus deleting the character before it.
# Inputs: "#a#b", "aa##", "##aa" output: "b", "" , "aa"

input = "##bb##"
output = []
for i in input:
    if i == "#" and output != []:
        output.pop()
    elif i != "#":
        output.append(i)

optStr = ""
for i in output:
    optStr += i

print(optStr)