def helper(nums):
    isDecreasing = True
    for i in range(1, len(nums)):
        if i == 1:
            if nums[0] < nums[1]:
                isDecreasing = False
        if (
            isDecreasing and 
                (nums[i - 1] - nums[i] < 1 or nums[i - 1] - nums[i] > 3)
        ) or (
            not isDecreasing and 
                (nums[i] - nums[i - 1] < 1 or nums[i] - nums[i - 1] > 3)
        ):
            return False
    return True

with open("input-2.txt", "r") as file:
    ret = 0
    for line in file:
        nums = [int(x) for x in line.split(" ")]
        isGood = False
        for i in range(len(nums)):
            currTest = nums[:i] + nums[i + 1:]
            if helper(currTest):
                isGood = True
                break
        if isGood:
            ret += 1
    print(ret)