VISITED = '-1'

def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def explore(grid, x, y, currVal):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    bfs = [(x, y)]
    area, perimeter = 0, 0
    visited = set()
    visited.add((x, y))
    while bfs:
        x, y = bfs.pop(0)
        if grid[x][y] == currVal:
            area += 1
        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if isInBounds(grid, newX, newY) and grid[newX][newY] == currVal:
                if (newX, newY) not in visited:
                    visited.add((newX, newY))
                    bfs.append((newX, newY))
            else:
                perimeter += 1
    for x, y in visited:
        grid[x][y] = VISITED
    return (area, perimeter)

with open('input.txt') as file:
    grid = []
    for line in file.readlines():
        temp = []
        line = line.rstrip("\n")
        for c in line:
            temp.append(c)
        grid.append(temp)
    
    ret = 0
            
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != VISITED:
                area, perimeter = explore(grid, i, j, grid[i][j])
                ret += area * perimeter
    print(ret)