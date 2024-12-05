from collections import defaultdict
rules = defaultdict(list)

def processAndFixUpdate(line):
    nums = [int(x) for x in line.split(',')]
    # Bubble sort
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] in  rules[nums[j + 1]]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


    return nums[len(nums)//2]

def processRules(line):
    before, after = line.split("|")
    rules[int(before)].append(int(after))

def processUpdates(line):
    nums = [int(x) for x in line.split(',')]
    nums.reverse()
    blacklist = set()
    for num in nums:
        if num in blacklist:
            return processAndFixUpdate(line)
        for i in rules[num]:
            blacklist.add(i)
    return 0

with open('input.txt') as file:
    ret = 0
    for line in file.readlines():
        line = line.rstrip("\n")
        if "|" in line:
            processRules(line)
        elif "," in line:
            ret += processUpdates(line)
    print(ret)