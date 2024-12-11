import functools
from collections import Counter, defaultdict

@functools.cache
def helper(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        halfIndex = int(len(stone)/2)
        leftHalf = stone[:halfIndex]
        rightHalf = stone[halfIndex:]
        return [leftHalf, str(int(rightHalf))]
    else:
        return [str(int(stone) * 2024)]

with open('input.txt') as file:
    stones = []
    for line in file.readlines():
        line = line.rstrip("\n")
        for c in line.split(' '):
            stones.append(c)
    
    stones = Counter(stones)

    for i in range(75):
        stone_counter = defaultdict(int)
        for stone in stones.keys():
            for val in helper(stone):
                stone_counter[val] += stones[stone]
        stones = stone_counter
        print("Iter " + str(i) + ": " + str(sum(stones.values())))