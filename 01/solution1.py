with open("input-1.txt", "r") as file:
    firstArr = []
    secondArr = []
    for line in file:
        a, b = line.split("   ")
        firstArr.append(int(a))
        secondArr.append(int(b))
    firstArr.sort()
    secondArr.sort()
    ret = 0
    for i in range(len(firstArr)):
        ret += abs(firstArr[i] - secondArr[i])
    print(ret)
