from collections import defaultdict
with open("input-2.txt", "r") as file:
    firstArr = []
    freqMap = defaultdict(int)
    for line in file:
        a, b = line.split("   ")
        firstArr.append(int(a))
        freqMap[int(b)] += 1
    ret = 0
    for i in range(len(firstArr)):
        ret += firstArr[i] * freqMap[firstArr[i]]
    print(ret)