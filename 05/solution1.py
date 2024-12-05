from collections import defaultdict
rules = defaultdict(list)

def processRules(line):
    before, after = line.split("|")
    rules[int(before)].append(int(after))


def processUpdates(line):
    nums = [int(x) for x in line.split(',')]
    nums.reverse()
    blacklist = set()
    for num in nums:
        if num in blacklist:
            return 0
        for i in rules[num]:
            blacklist.add(i)
    return nums[len(nums)//2]


with open('input.txt') as file:
    ret = 0
    for line in file.readlines():
        line = line.rstrip("\n")
        if "|" in line:
            processRules(line)
        elif "," in line:
            ret += processUpdates(line)
    print(ret)