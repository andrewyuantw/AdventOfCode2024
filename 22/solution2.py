from collections import defaultdict
with open('input.txt') as file:
    seqMap = defaultdict(int)
    
    def mix(a, b):
        return a ^ b
    def prune(a):
        return a % 16777216
    ret = 0
    for line in file.readlines():
        soldMap = defaultdict(bool)
        num = int(line)
        prev = int(str(num)[-1])
        seq = []
        for _ in range(2000):
            num = prune(mix(num, num * 64))
            num = prune(mix(num, int(num/32)))
            num = prune(mix(num, num * 2048))
            newLastDigit = int(str(num)[-1])
            delta = newLastDigit - prev
            seq.append(str(delta))
            if len(seq) == 4:
                key = ",".join(seq)
                if not soldMap[key]:
                    seqMap[key] += newLastDigit
                    soldMap[key] = True
                seq.pop(0)
            prev = newLastDigit
    lst = seqMap.values()
    print(max(lst))
