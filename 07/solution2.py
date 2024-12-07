import time
start = time.time()

def helper(currSum, target, arr):
    if len(arr) == 0:
        return currSum == target
    return (
        helper(currSum + arr[0], target, arr[1:]) or 
        helper(currSum * arr[0], target, arr[1:]) or
        helper(int(str(currSum) + str(arr[0])), target, arr[1:])
    )
    
with open('input.txt') as file:
    ret = 0
    for line in file.readlines():
        line = line.rstrip("\n")
        result, allNums = line.split(": ")
        nums = [int(x) for x in allNums.split(' ')]
        if helper(nums[0], int(result), nums[1:]):
            ret += int(result)
    print(ret)

end = time.time()
print(end - start)