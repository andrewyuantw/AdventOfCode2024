import numpy as np

with open('input.txt') as file:
    ret = 0
    xA, yA, xB, yB, prizeX, prizeY = 0, 0,0,0,0,0
    for line in file.readlines():
        line = line.rstrip("\n")
        if line.startswith("Button A"):
            xA , yA = [int(x) for x in line[len("Button A: X"):].split(", Y")]
        elif line.startswith("Button B"):
            xB , yB = [int(x) for x in line[len("Button B: X"):].split(", Y")]
        elif line.startswith("Prize"):
            prizeX, prizeY = [int(x) for x in line[len("Prize: X="):].split(", Y=")]
            a = np.array([[xA, xB], [yA, yB]])
            b = np.array([prizeX, prizeY])
            apush, bpush = [round(x) for x in np.linalg.solve(a, b)]
            if (np.dot(a, np.array([apush, bpush])) == b).all():
                ret += 3 * apush + bpush
    print(ret)