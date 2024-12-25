with open('input.txt') as file:
    def mix(a, b):
        return a ^ b
    def prune(a):
        return a % 16777216
    ret = 0
    for line in file.readlines():
        
        num = int(line)
        for _ in range(2000):
            num = prune(mix(num, num * 64))
            num = prune(mix(num, int(num/32)))
            num = prune(mix(num, num * 2048))
        ret += num
    print(ret)
