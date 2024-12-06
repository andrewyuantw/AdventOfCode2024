def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

with open("input.txt", "r") as file:
    
    grid = []
    for line in file:
        temp = []
        for c in line:
            temp.append(c)
        grid.append(temp)

    allDirections = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Found starting point, now start walking
            if grid[i][j] == '^':
                startingX, startingY = i, j
                currDirectionIndex = 0
                # while still in the maze
                while isInBounds(grid, startingX, startingY):
                    # Visit current spot
                    grid[startingX][startingY] = 'X'
                    # Now find valid next spot
                    diffX, diffY = allDirections[currDirectionIndex % 4]
                    nextX, nextY = startingX + diffX, startingY + diffY
                    # If the next spot is obstacle, turn in next direction
                    if isInBounds(grid, nextX, nextY) and grid[nextX][nextY] == '#':
                        currDirectionIndex += 1
                        diffX, diffY = allDirections[currDirectionIndex % 4]
                        nextX, nextY = startingX + diffX, startingY + diffY
                    startingX, startingY = nextX, nextY
                
                # Exited the grid, count X's
                ret = sum([row.count('X') for row in grid])
                print(ret)