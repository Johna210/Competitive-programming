def addSpaces(s, spaces):
    edited = ""
    start = 0
    for i in spaces:
        edited += s[start:i] + " "
        start = i
    edited += s[start:]
    return edited


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

s2 = "icodeinpython" 
spaces2 = [1,5,7,9]

s3 = "spacing"
spaces3 = [0,1,2,3,4,5,6]

print(addSpaces(s,spaces))
print(addSpaces(s2,spaces2))
print(addSpaces(s3,spaces3))
