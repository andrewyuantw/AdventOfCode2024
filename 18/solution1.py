SIDE = 71
NUM_CORRUPT_BYTES = 1024

def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open('input.txt') as file:
    counter = 0
    grid = []
    for _ in range(SIDE):
        grid.append(["."] * SIDE)
    for line in file.readlines():
        if counter == NUM_CORRUPT_BYTES:
            break
        a, b = [int(x) for x in line.split(",")]
        grid[b][a] = "#"
        counter += 1
    for row in grid:
        print("".join(row))
    bfs = [(0, 0, 0)]
    ret = float('inf')
    visited = set()
    visited.add((0, 0))
    while bfs:
        x, y, steps = bfs.pop(0)
        if x == SIDE - 1 and y == SIDE - 1:
            ret = min(ret, steps)

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if isInBounds(grid, newX, newY) and (newX, newY) not in visited and grid[newX][newY] != "#":
                bfs.append((newX, newY, steps + 1))
                visited.add((newX, newY))
    print(ret)