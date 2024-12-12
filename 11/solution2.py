import functools

@functools.cache
def helper(stone, iter):
    if iter == 0:
        return 1
    if stone == '0':
        return helper('1', iter - 1)
    elif len(stone) % 2 == 0:
        halfIndex = int(len(stone)/2)
        leftHalf = stone[:halfIndex]
        rightHalf = stone[halfIndex:]
        return helper(leftHalf, iter - 1) + helper(str(int(rightHalf)), iter - 1)
    else:
        return helper(str(int(stone) * 2024), iter - 1)

with open('input.txt') as file:
    stones = []
    for line in file.readlines():
        line = line.rstrip("\n")
        for c in line.split(' '):
            stones.append(c)
    ret = 0
    for stone in stones:
        ret += helper(stone, 75)
    print(ret)