def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def explore(grid, x, y, currVal, trailEnds):
    if currVal == 9:
        trailEnds.add((x, y))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        if isInBounds(grid, newX, newY):
            if grid[newX][newY] == currVal + 1:
                explore(grid, newX, newY, currVal + 1, trailEnds)

with open('input.txt') as file:
    grid = []
    for line in file.readlines():
        temp = []
        line = line.rstrip("\n")
        for c in line:
            temp.append(int(c))
        grid.append(temp)
    
    ret = 0
            
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailEnds = set()
                explore(grid, i, j, 0, trailEnds)
                ret += len(trailEnds)
    print(ret)