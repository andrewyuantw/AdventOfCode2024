from collections import defaultdict

emptySpaces = []
emptySpacesIndex = []

with open('input.txt') as file:
    ret = 0
    arr = []
    id_counter = 0
    prefixSum = [0]
    for line in file.readlines():
        firstLine = line
        isFree = False
        for c in line:
            i = int(c)
            prefixSum.append(prefixSum[-1] + i)
            for _ in range(i):
                if isFree:
                    arr.append(".")
                else:
                    arr.append(id_counter)
            if isFree:
                emptySpaces.append(i)
                emptySpacesIndex.append(len(arr) - i)
                isFree = False
            else:
                isFree = True
                id_counter += 1
        isFree = False
        for i in range(len(line) - 1, -1, -1):
            if not isFree:
                neededEmptySpaces = int(line[i])
                # Find first spot
                for j in range(len(emptySpaces)):
                    currSpace = emptySpaces[j]
                    if currSpace >= neededEmptySpaces:
                        # Check if before current index
                        currentIndex = prefixSum[i + 1] - neededEmptySpaces
                        if currentIndex < emptySpacesIndex[j]:
                            break
                        # Update arr
                        slotStartingIndex = emptySpacesIndex[j]
                        for k in range(neededEmptySpaces):
                            arr[slotStartingIndex + k], arr[currentIndex + k] =  arr[currentIndex + k], arr[slotStartingIndex + k]
                        # Update slots
                        emptySpaces[j] -= neededEmptySpaces
                        emptySpacesIndex[j] += neededEmptySpaces

                        if emptySpaces[j] <= 0:
                            emptySpaces.pop(j)
                            emptySpacesIndex.pop(j)
                        break

                id_counter -= 1
            isFree = not isFree
        for i in range(len(arr)):
            if arr[i] != ".":
                ret += arr[i] * i
        print(ret)