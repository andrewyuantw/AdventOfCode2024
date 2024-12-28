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

def lookupIndex(c, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == c:
                return (i, j)
    return (0,0)

def shortestPath(prev, dest, grid):
    prevX, prevY = lookupIndex(prev, grid)
    destX, destY = lookupIndex(dest, grid)

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

def bestSequence(code, grid):
    ret = []
    prev = "A"
    for c in code:
        ret.append(shortestPath(prev, c, grid))
        prev = c
    return ret

with open('input.txt') as file:
    input = file.read()
    codes = input.split("\n")
    ret = 0
    k1codes = ["".join(bestSequence(c, numPad)) for c in codes]
    k2codes = ["".join(bestSequence(c, dirPad)) for c in k1codes]
    k3codes = ["".join(bestSequence(c, dirPad)) for c in k2codes]
    for i in range(len(k3codes)):
        numInInit = int(codes[i][:-1])
        ret += numInInit * len(k3codes[i])
    print(ret)