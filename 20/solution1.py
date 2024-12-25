AMOUNT_TO_SAVE = 100

def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

with open('input.txt') as file:
    grid = []
    for line in file.readlines():
        line = line.rstrip("\n")
        temp = []
        for c in line:
            temp.append(c)
        grid.append(temp)
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                bfs = []
                bfs = [(i, j, 0)]
                visited = set()
                visited.add((i, j))
                
                while bfs:
                    x, y, steps = bfs.pop(0)
                    grid[x][y] = str(steps)
                    for dir_index in range(len(directions)):
                        dx, dy = directions[dir_index]
                        newX, newY = x + dx, y + dy
                        if grid[newX][newY] != '#' and ((newX, newY) not in visited):
                            bfs.append((newX, newY, steps + 1))
                            
                            visited.add((newX, newY))
    ret = 0
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "#":
                startingTime = int(grid[i][j])
                for dx, dy in directions:
                    newX, newY = i + dx, j + dy
                    if isInBounds(grid, newX, newY) and grid[newX][newY] != '#':
                        newTime = int(grid[newX][newY])
                        if newTime - startingTime >= AMOUNT_TO_SAVE + 2:
                            ret += 1
    print(ret)