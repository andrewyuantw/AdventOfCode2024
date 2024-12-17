HEIGHT = 103
WIDTH = 101
NUM_STEPS = 6446

with open('input.txt') as file:
    q1, q2, q3, q4 = 0, 0, 0, 0
    positions = []
    velocities = []
    for line in file.readlines():
        temp = []
        line = line.rstrip("\n")
        position, velocity = line.split(" ")
        posX, posY = [int(x) for x in position[2:].split(",")]
        velX, velY = [int(x) for x in velocity[2:].split(",")]
        positions.append((posX, posY))
        velocities.append((velX, velY))

    for step in range(NUM_STEPS):
        # Update the positions
        for i in range(len(positions)):
            posX, posY = positions[i]
            velX, velY = velocities[i]
            newX, newY = (posX + velX) % WIDTH, (posY + velY) % HEIGHT
            positions[i] = (newX, newY)


        positionSet = set(positions)
        # Find right corner
        for i in range(len(positions)):
            x, y = positions[i]
            isGoodCorner = True
            TREE_CORNER_LENGTH = 5
            for z in range(TREE_CORNER_LENGTH):
                if not ((x + z, y) in positionSet and (x, y - z) in positionSet):
                    isGoodCorner = False
                    break
            if isGoodCorner:
                # We found a right corner at depth y, can we find left corner
                for j in range(len(positions)):
                    a, b = positions[j]
                    if b == y and abs(x - a) > 10:
                        for z in range(TREE_CORNER_LENGTH):
                            if not ((a - z, b) in positionSet and (a, b - z) in positionSet):
                                isGoodCorner = False
                                break
                        if isGoodCorner:
                            print(step)
    
    grid = []
    for _ in range(HEIGHT):
        grid.append(["."] * WIDTH)
    for x, y in positions:
        grid[y][x] = "1"
    for row in grid:
        print("".join(row))
    
    
    
    