from collections import defaultdict
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
    print(int(ret, 2))

