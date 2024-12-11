def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def explore(grid, x, y, currVal):
    if currVal == 9:
        return 1
    ret = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        if isInBounds(grid, newX, newY):
            if grid[newX][newY] == currVal + 1:
                ret += explore(grid, newX, newY, currVal + 1)
    return ret

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
                ret += explore(grid, i, j, 0)
    print(ret)