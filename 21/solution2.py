from functools import cache

numPad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"], 
    ["", "0", 'A']
]

dirPad = [
    ["", "^", "A"],
    ["<", "v", ">"]
]

NUMPADNUM = 0
DIRPADNUM = 1

@cache
def lookupIndex(c, gridNum):
    grid = dirPad if gridNum == DIRPADNUM else numPad
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == c:
                return (i, j)
    return (0,0)

@cache
def shortestPath(prev, dest, gridNum):
    grid = dirPad if gridNum == DIRPADNUM else numPad
    prevX, prevY = lookupIndex(prev, gridNum)
    destX, destY = lookupIndex(dest, gridNum)

    # Best paths are not going to cancel movements (v and then ^)
    # Best paths also should not switch keys (vv> preferred over v>v)

    deltaX = destX - prevX
    deltaXChangeString = "v" * deltaX if deltaX > 0 else "^" * (-deltaX)
    deltaY = destY - prevY
    deltaYChangeString = ">" * deltaY if deltaY > 0 else "<" * (-deltaY)

    # Move along x first or y first?
    # Prefer to process > as little as possible as transitioning from > would require
    # < to be pressed on the next keyboard which is expensive
    if deltaY <= 0 and grid[destX][prevY] != "":
        if grid[prevX][destY] == "":
            return deltaXChangeString + deltaYChangeString + "A"
        return deltaYChangeString + deltaXChangeString + "A"
    else:
        if grid[destX][prevY] == "":
            return deltaYChangeString + deltaXChangeString + "A"
        return deltaXChangeString + deltaYChangeString + "A"

@cache
def bestSequence(code, grid):
    ret = []
    prev = "A"
    for c in code:
        ret.append(shortestPath(prev, c, grid))
        prev = c
    return ret

@cache
def bestLength(code, recursiveDepth, firstLayer):
    if recursiveDepth < 0:
        return len(code) 
    gridNum = NUMPADNUM if firstLayer else DIRPADNUM
    ret = 0
    prev = "A"
    for c in code:
        ret += bestLength(shortestPath(prev, c, gridNum), recursiveDepth - 1, False)
        prev = c
    return ret

with open('input.txt') as file:
    input = file.read()
    codes = input.split("\n")
    ret = 0
    keycodes = ["".join(bestSequence(c, NUMPADNUM)) for c in codes]

    for code in codes:
        numInInit = int(code[:-1])
        newCodeLength = bestLength(code, 25, True)
        ret += numInInit * newCodeLength
    print(ret)