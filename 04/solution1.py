def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

def exploreHelper(grid, startingX, startingY, xDiff, yDiff, word):
    if word == "":
        return 1
    if not isInBounds(grid, startingX, startingX):
        return 0
    if grid[startingX][startingY] != word[0]:
        return 0
    return exploreHelper(grid, startingX + xDiff, startingY + yDiff, xDiff, yDiff, word[1:])

allDirections = [(1, 0), (-1, 0), (0, 1), (0, -1), (1,1), (1, -1), (-1, 1), (-1, -1)]

with open("input.txt", "r") as file:
    ret = 0
    grid = []
    for line in file:
        grid.append(line)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Do exploration
            if grid[i][j] == 'X':
                ret += sum([exploreHelper(grid, i, j, x, y, "XMAS") for x, y in allDirections])
    print(ret)