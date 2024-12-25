from collections import defaultdict
with open('input.txt') as file:
    connections = defaultdict(set)
    for line in file.readlines():
        line = line.rstrip("\n")
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)
    checked = set()
    ret = []
    for key in connections.keys():
        partners = connections[key]
        secondChecked = set()
        for partner in partners:
            if partner in checked:
                continue
            partnerSet = connections[partner]
            
            for i in partnerSet:
                if i in partners and i not in checked and i not in secondChecked:
                    ret.append([i, partner, key])
                    secondChecked.add(partner)
        checked.add(key)
    ans = 0
    for pair in ret:
        for i in pair:
            if i[0] == 't':
                ans += 1
                break
    print(ans)
