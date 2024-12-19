from collections import defaultdict
import functools

with open('input.txt') as file:

    
    counter = 0
    options = []
    desired_patterns = []
    for line in file.readlines():
        line = line.rstrip("\n")
        if counter == 0:
            options = line.split(", ")
        elif counter >= 2:
            desired_patterns.append(line)
        counter += 1
    ret = 0

    optionMap = defaultdict(list)
    for option in options:
        optionMap[option[0]].append(option)

    @functools.cache
    def helper(pat):
        ret = 0
        if pat == "":
            return True
        option_to_use = optionMap[pat[0]]
        for opt in option_to_use:
            if opt == pat[:len(opt)]:
                ret += helper(pat[len(opt):])
        return ret

    for pat in desired_patterns:
        ret += helper(pat)
    print(ret)