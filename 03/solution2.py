import re

def helper(s):
    ret = 0
    regexPattern = re.compile(r'mul\([0-9]*,[0-9]*\)')
    finds = regexPattern.findall(s)
    ret += sum([int(s[s.index("(") + 1: s.index(",")]) * int(s[s.index(",") + 1: s.index(")")]) for s in finds])
    return ret

with open("input-2.txt", "r") as file:
    ret = 0
    for line in file:
        cleanedLine = ""
        # while there are disabled sections
        while line.find("don't()") != -1:
            # find start of disabled section
            dontIndex = line.find("don't()")
            cleanedLine += line[:dontIndex]
            line = line[dontIndex + 1:] 
            # find end of disabled section
            doIndex = line.find("do()")
            if doIndex == -1:
                line = ""
            elif doIndex != -1:
                line = line[doIndex + 1:]
        if line:
            cleanedLine += line
        ret += helper(cleanedLine)
    print(ret)