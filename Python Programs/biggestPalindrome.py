# For a given input string "aabccdccbaa",
# find the biggest palindrom, 
# which is "aabccdccbaa", not "ccdcc" or "bccdccb" or ...others


def expandFromCenter(s, left, right):
    if s == "":
        return 0
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1



def findPalindrome(s):
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expandFromCenter(s, i, i)
        len2 = expandFromCenter(s, i, i+1)
        palLen = max(len1, len2)
        if palLen > end - start :
            start = i - (int)((palLen - 1)/2)
            end = i + (int)(palLen / 2)
    
    return s[start : end+1]

s = input("Enter a string: ")

subs = findPalindrome(s)

print(subs)