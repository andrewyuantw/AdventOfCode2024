with open('input.txt') as file:
    stones = []
    for line in file.readlines():
        line = line.rstrip("\n")
        for c in line.split(' '):
            stones.append(c)
    
    for _ in range(25):
        next_stones = []
        for stone in stones:
            if stone == '0':
                next_stones.append('1')
            elif len(stone) % 2 == 0:
                halfIndex = int(len(stone)/2)
                leftHalf = stone[:halfIndex]
                rightHalf = stone[halfIndex:]
                next_stones.append(leftHalf)
                next_stones.append(str(int(rightHalf)))
            else:
                next_stones.append(str(int(stone) * 2024))
        stones = next_stones
    print(len(stones))