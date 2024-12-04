def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def exploreHelper(grid, startingX, startingY):
    diagonals = [(1, 1), (-1, 1)]
    for xDiff, yDiff in diagonals:
        wordSet = set(["M", "S"])
        endpoint1x, endpoint1y = startingX + xDiff, startingY + yDiff
        endpoint2x, endpoint2y = startingX - xDiff, startingY - yDiff

        if not (isInBounds(grid, endpoint1x, endpoint1y) and isInBounds(grid, endpoint2x, endpoint2y)):
            return 0
        diagonalContent = [grid[endpoint1x][endpoint1y], grid[endpoint2x][endpoint2y]]
        if set(diagonalContent) != wordSet:
            return 0
    return 1

with open("input.txt", "r") as file:
    ret = 0
    grid = []
    for line in file:
        grid.append(line)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Do exploration
            if grid[i][j] == 'A':
                ret += exploreHelper(grid, i, j)
    print(ret)