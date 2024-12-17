import time
def executeMovements(grid, movements, x, y):
    movementMap = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
    accu = ""
    for move in movements:
        accu += move
        dX, dY = movementMap[move]
        newX, newY = x + dX, y + dY
        if grid[newX][newY] == '#':
            continue
        elif grid[newX][newY] == '.':
            grid[newX][newY] = "@"
            grid[x][y] = '.'
            x, y = newX, newY
        else:
            # Get the effective movement surface
            movementSurface = []
            if grid[newX][newY] == '[':
                if move == ">":
                    movementSurface.append((newX, newY + 1))
                elif move == "^" or move == "v":
                    movementSurface.append((newX, newY))
                    movementSurface.append((newX, newY + 1))
            elif grid[newX][newY] == ']':
                if move == "<":
                    movementSurface.append((newX, newY - 1))
                elif move == "^" or move == "v":
                    movementSurface.append((newX, newY - 1)) 
                    movementSurface.append((newX, newY))
                    
            
            # Get the boxes that we've accumulated so far
            accumulatedBoxes = []
            if grid[newX][newY] == '[':
                accumulatedBoxes.append((newX, newY))
                accumulatedBoxes.append((newX, newY + 1))
            elif grid[newX][newY] == ']':
                accumulatedBoxes.append((newX, newY))
                accumulatedBoxes.append((newX, newY - 1))
                 
            
            # Calculate needed clear space to move (all of movementSurface needs to have space)
            neededClearSpace = []
            for i, j in movementSurface:
                neededClearSpace.append((i + dX, j + dY))

            while True:
                # Scenario 1: No space to move, stop
                noClearSpace = False
                for i, j in neededClearSpace:
                    if grid[i][j] == '#':
                        noClearSpace = True
                        break
                if noClearSpace:
                    break
                
                # Scenario 2: Found clear space, now update the grid
                isAllClear = True
                for i, j in neededClearSpace:
                    if grid[i][j] != '.':
                        isAllClear = False
                        break
                if isAllClear:
                    # Update the grid
                    accumulatedBoxes.reverse()
                    for i, j in accumulatedBoxes:
                        grid[i + dX][j + dY] = grid[i][j]
                        grid[i][j] = '.'
                    grid[x+ dX][y + dY] = "@"
                    grid[x][y] = '.'
                    x, y = x+ dX, y + dY
                    break

                # Scenario 3: Accumulated more boxes
                # update movementSurface, accumulatedBoxes, neededClearSpace
                newBoxes = set()
                newBoxesList = []
                newMovementSurface = set()
                for i, j in movementSurface:
                    newX, newY = i + dX, j + dY
                    if grid[newX][newY] == '[':
                        if (newX, newY) not in newBoxes:
                            newBoxes.add((newX, newY))
                            newBoxesList.append((newX, newY))
                        if (newX, newY + 1) not in newBoxes:
                            newBoxes.add((newX, newY + 1))
                            newBoxesList.append((newX, newY + 1))
                    elif grid[newX][newY] == ']':
                        if (newX, newY) not in newBoxes:
                            newBoxes.add((newX, newY))
                            newBoxesList.append((newX, newY))
                        if (newX, newY - 1) not in newBoxes:
                            newBoxes.add((newX, newY - 1))
                            newBoxesList.append((newX, newY - 1))
                        
                    if grid[newX][newY] == '[':
                        if move == ">":
                            newMovementSurface.add((newX, newY + 1))
                        elif move == "^" or move == "v":
                            newMovementSurface.add((newX, newY))
                            newMovementSurface.add((newX, newY + 1))
                    elif grid[newX][newY] == ']':
                        if move == "<":
                            newMovementSurface.add((newX, newY - 1))
                        elif move == "^" or move == "v":
                            newMovementSurface.add((newX, newY - 1)) 
                            newMovementSurface.add((newX, newY))
                            
                accumulatedBoxes += newBoxesList
                movementSurface = list(newMovementSurface)
                neededClearSpace = []
                for i, j in movementSurface:
                    neededClearSpace.append((i + dX, j + dY))


        

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
                if c == "#":
                    temp.append("#")
                    temp.append("#")
                elif c == ".":
                    temp.append(".")
                    temp.append(".")
                elif c == "O":
                    temp.append("[")
                    temp.append("]")
                else:
                    temp.append("@")
                    temp.append(".")
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
    for row in grid:
        print("".join(row))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                ret += 100 * i + j
    print(ret)