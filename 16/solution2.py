from collections import defaultdict

# Store map of scores -> list of paths (paths being list of nodes visited)

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
                visitedCost = defaultdict(lambda: float('inf'))
                mapOfScores = defaultdict(list)
                bfs = []
                bfs = [(i, j, 0, 2, [(i, j)])]
                visited = set()
                visited.add((i, j))
                visitedCost[(i, j)] = 0
                while bfs:
                    x, y, score, currDirectionIndex, currentExplorationPath = bfs.pop(0)
                    if grid[x][y] == 'E':
                        mapOfScores[score].append(currentExplorationPath)
                        ret = min(score, ret)
                    for dir_index in range(len(directions)):
                        dx, dy = directions[dir_index]
                        newX, newY = x + dx, y + dy
                        newScore = score + 1 if dir_index == currDirectionIndex else score + 1001
                        if grid[newX][newY] != '#' and ((newX, newY) not in visited or newScore <= visitedCost[(newX, newY, dir_index)]):
                            path_copy = currentExplorationPath.copy()
                            path_copy.append((newX, newY))
                            bfs.append((newX, newY, newScore, dir_index, path_copy))
                            visited.add((newX, newY))
                            visitedCost[(newX, newY, dir_index)] = newScore
                bestSeats = sum(mapOfScores[ret], [])
                for x, y in bestSeats:
                    grid[x][y] = "O"
                for row in grid:
                    print("".join(row))
                print(len(set(bestSeats)))
                break