def executeMovements(grid, movements, x, y):
    movementMap = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
    counter = 0
    for move in movements:
        counter += 1
        dX, dY = movementMap[move]
        newX, newY = x + dX, y + dY
        if grid[newX][newY] == '#':
            continue
        elif grid[newX][newY] == '.':
            grid[newX][newY] = "@"
            grid[x][y] = '.'
            x, y = newX, newY
        else:
            newX += dX
            newY += dY
            while True:
                if grid[newX][newY] == '#':
                    break
                if grid[newX][newY] == '.':
                    grid[newX][newY] = "O"
                    grid[x+ dX][y + dY] = "@"
                    grid[x][y] = '.'
                    x, y = x+ dX, y + dY
                    break
                newX += dX
                newY += dY
        

with open('input.txt') as file:
    grid = []
    movements = ""
    foundBreak = False
    for line in file.readlines():
        if line == "\n":
            foundBreak = True
            continue
        if not foundBreak:
            temp = []
            line = line.rstrip("\n")
            for c in line:
                temp.append(c)
            grid.append(temp)
        else:
            movements += line.rstrip("\n")
    
    ret = 0
    startingX, startingY = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                startingX, startingY = i, j
    executeMovements(grid, movements, startingX, startingY)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                ret += 100 * i + j
    print(ret)