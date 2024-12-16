from collections import defaultdict

with open('input.txt') as file:
    grid = []
    for line in file.readlines():
        line = line.rstrip("\n")
        temp = []
        for c in line:
            temp.append(c)
        grid.append(temp)
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ret = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                visitedCost = defaultdict(int)
                bfs = []
                bfs = [(i, j, 0, 2)]
                visited = set()
                visited.add((i, j))
                visitedCost[(i, j)] = 0
                while bfs:
                    x, y, score, currDirectionIndex = bfs.pop(0)
                    if grid[x][y] == 'E':
                        ret = min(score, ret)
                    for dir_index in range(len(directions)):
                        dx, dy = directions[dir_index]
                        newX, newY = x + dx, y + dy
                        newScore = score + 1 if dir_index == currDirectionIndex else score + 1001
                        if grid[newX][newY] != '#' and ((newX, newY) not in visited or newScore < visitedCost[(newX, newY)] ):
                            bfs.append((newX, newY, newScore, dir_index))
                            visited.add((newX, newY))
                            visitedCost[(newX, newY)] = newScore
    print(ret)