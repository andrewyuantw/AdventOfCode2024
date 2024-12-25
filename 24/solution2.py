from collections import defaultdict
'''
Manual solve for me on this problem,
below is the code I used to isolate the four digits
that were incorrect. After that, I looked at a correct digit
to find the pattern of the five logic gates.

Once I knew that, I then manually traced through the incorrect
digit gates and was able to find the swaps.
'''
with open('input.txt') as file:
    isGate = False
    mapOfValues = defaultdict(int)
    mapOps = defaultdict(list)
    for line in file.readlines():
        if line == "\n":
            isGate = True
            continue
        line = line.rstrip("\n")
        if not isGate:
            a, b = line.split(": ")
            mapOfValues[a] = int(b)
        else:
            a, b = line.split(" -> ")
            mapOps[b] = a.split(" ")
    
    NUMVAR = 45

    SAME = 2 ** 36
    NUM1 = SAME
    NUM2 = 0

    num1 = '{:045b}'.format(NUM1)
    num2 = '{:045b}'.format(NUM2)

    for i in range(NUMVAR):
        keyX = "x" + "{:02d}".format(i)
        keyY = "y" + "{:02d}".format(i)
        mapOfValues[keyX] = int(num1[NUMVAR - 1 - i])
        mapOfValues[keyY] = int(num2[NUMVAR - 1 - i])

    INVOLVED_KEY = 'z13'

    involved = set()
    involved.add(INVOLVED_KEY)
    explore = [INVOLVED_KEY]

    while explore:
        curr = explore.pop(0)
        if curr in mapOfValues:
            continue
        a, op ,b = mapOps[curr]
        if a not in involved:
            explore.append(a)
            involved.add(a)
        if b not in involved:
            explore.append(b)
            involved.add(b)
    print(involved)

    

    while mapOps:
        lstKey = list(mapOps.keys())
        for key in lstKey:
            a, op ,b = mapOps[key]
            if a in mapOfValues and b in mapOfValues:
                # can evaluate
                if op == 'AND':
                    mapOfValues[key] = mapOfValues[a] & mapOfValues[b]
                elif op == 'XOR':
                    mapOfValues[key] = mapOfValues[a] ^ mapOfValues[b]
                elif op == "OR":
                    mapOfValues[key] = mapOfValues[a] | mapOfValues[b]
                del mapOps[key]
    ret = ""
    lstKey = list(mapOfValues.keys())
    lstKey.sort()
    for key in lstKey:
        if key[0] == 'z':
            ret = str(mapOfValues[key]) + ret
            if str(mapOfValues[key]) == '1':
                print(key)
    print(ret)
    print('{:046b}'.format(NUM1 + NUM2))
    print(int(ret, 2))

