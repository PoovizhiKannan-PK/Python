# For a given input string = "a-bc-def" reverse only the letters in it.
# Output = "f-ed-cba"

str1 = "a-bC-dEf-gHIj"
start = 0
end = len(str1) -1

str1 = list(str1)

while(start < end):
    if not (str1[start].isalpha()):
        start += 1
    if not (str1[end].isalpha()):
        end -= 1

    str1[start], str1[end] = str1[end], str1[start]
    start += 1
    end -= 1


print("".join([str(e) for e in str1]))