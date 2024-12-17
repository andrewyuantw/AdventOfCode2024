HEIGHT = 103
WIDTH = 101
NUM_STEPS = 100

with open('input.txt') as file:
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in file.readlines():
        temp = []
        line = line.rstrip("\n")
        position, velocity = line.split(" ")
        posX, posY = [int(x) for x in position[2:].split(",")]
        velX, velY = [int(x) for x in velocity[2:].split(",")]
        finalX, finalY = (posX + velX * NUM_STEPS) % WIDTH, (posY + velY * NUM_STEPS) % HEIGHT
        if finalX < int(WIDTH/2):
            if finalY < int(HEIGHT/2):
                q2 += 1
            elif finalY > int(HEIGHT/2):
                q4 += 1
        elif finalX > int(WIDTH/2):
            if finalY < int(HEIGHT/2):
                q1 += 1
            elif finalY > int(HEIGHT/2):
                q3 += 1
    print(q1 * q2 * q3 * q4)