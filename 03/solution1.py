import re

with open("input-1.txt", "r") as file:
    ret = 0
    regexPattern = re.compile(r'mul\([0-9]*,[0-9]*\)')
    for line in file:
        finds = regexPattern.findall(line)
        ret += sum([int(s[s.index("(") + 1: s.index(",")]) * int(s[s.index(",") + 1: s.index(")")]) for s in finds])
    print(ret)