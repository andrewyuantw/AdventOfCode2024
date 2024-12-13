VISITED = '-1'

def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def explore(grid, x, y, currVal):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    bfs = [(x, y)]
    area, corners = 0, 0
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
        for i in range(len(directions)):
            side1dx, side1dy = directions[i]
            side2dx, side2dy = directions[(i + 1) % 4]
            
            side1x, side1y = x + side1dx, y + side1dy
            side2x, side2y = x + side2dx, y + side2dy 
            diagx, diagy = x + side1dx + side2dx, y + side1dy + side2dy

            isSide1Corner = not isInBounds(grid, side1x, side1y) or grid[side1x][side1y] != currVal
            isSide2Corner = not isInBounds(grid, side2x, side2y) or grid[side2x][side2y] != currVal
            isDiagCorner = isInBounds(grid, diagx, diagy) and grid[diagx][diagy] != currVal

            if isSide1Corner and isSide2Corner or (not isSide1Corner and not isSide2Corner and isDiagCorner) :
                corners += 1


    for x, y in visited:
        grid[x][y] = VISITED
    return (area, corners)

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
                area, sides = explore(grid, i, j, grid[i][j])
                ret += area * sides
    print(ret)