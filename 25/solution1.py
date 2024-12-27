with open('input.txt') as file:
    data = file.read()
    locks = []
    keys = []
    isNew = True
    chunks = data.split("\n\n")
    for chunk in chunks:
        chunk = chunk.split("\n")
        if chunk[0][0] == '#':
            # is a lock
            currLock = [0,0,0,0,0]
            for i in range(1, len(chunk)):
                for j in range(len(chunk[i])):
                    if chunk[i][j] == '#':
                        currLock[j] += 1
            locks.append(currLock)
        else:
            # is a key
            currKey = [0,0,0,0,0]
            for i in range(len(chunk) -2, -1, -1):
                for j in range(len(chunk[i])):
                    if chunk[i][j] == '#':
                        currKey[j] += 1
            keys.append(currKey)
    
    ret = 0

    
    for lock in locks:
        for key in keys:
            goodCombo = True
            for i in range(5):
                if lock[i] + key[i] > 5:
                    goodCombo = False
                    break
            if goodCombo:
                ret += 1
    print(ret)