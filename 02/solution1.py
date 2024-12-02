with open("input-1.txt", "r") as file:
    ret = 0
    for line in file:
        nums = [int(x) for x in line.split(" ")]
        isDecreasing = True
        isGood = True
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
                isGood = False
                break
        if isGood:
            ret += 1

    print(ret)