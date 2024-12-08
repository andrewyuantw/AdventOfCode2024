from collections import defaultdict

def isInBounds(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return False
    return True

with open('input.txt') as file:
    antinodes = set()
    grid = []
    symbolLocations = defaultdict(list)
    for line in file.readlines():
        temp = []
        line = line.rstrip("\n")
        for c in line:
            symbolLocations[c].append((len(grid), len(temp)))
            temp.append(c)
        grid.append(temp)
            
    symbolLocations['.'] = []
    
    for symbol in symbolLocations.keys():
        # Get every pair
        for i in range(len(symbolLocations[symbol])):
            for j in range(i + 1, len(symbolLocations[symbol])):
                
                # Check both antinode possible locations
                node1x, node1y = symbolLocations[symbol][i]
                node2x, node2y = symbolLocations[symbol][j]

                antinodes.add((node1x, node1y))
                antinodes.add((node2x, node2y))

                diffX, diffY = node2x - node1x, node2y - node1y

                location1X, location1Y = node1x - diffX, node1y - diffY
                while isInBounds(grid, location1X, location1Y):
                    antinodes.add((location1X, location1Y))
                    location1X, location1Y = location1X - diffX, location1Y - diffY
                location2X, location2Y = node2x + diffX, node2y + diffY
                while isInBounds(grid, location2X, location2Y):
                    antinodes.add((location2X, location2Y))
                    location2X, location2Y = location2X + diffX, location2Y + diffY
            
    print(len(antinodes))