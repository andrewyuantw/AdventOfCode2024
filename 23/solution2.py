from collections import defaultdict
with open('input.txt') as file:

    connections = defaultdict(set)
    for line in file.readlines():
        line = line.rstrip("\n")
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    # Returns the best "big" cluster including candidate being added to currCluster
    def helper(candidate, currCluster, visited):
        # First check if connected to everything in the cluster already
        check = currCluster.intersection(connections[candidate])
        if len(check) == len(currCluster):
            # passes the check, add it 
            currCluster.add(candidate)
            # look at new recruits
            bestCluster = currCluster
            for partner in connections[candidate]:
                if partner in currCluster or partner in visited:
                    continue
                clusterCopy = currCluster.copy()
                resCluster = helper(partner, clusterCopy, visited)
                if len(resCluster) > len(bestCluster):
                    bestCluster = resCluster
            visited.add(candidate)
            return bestCluster
        else:
            visited.add(candidate)
            return set()
        
    bestCluster = set()
    for key in connections.keys():
        partners = connections[key]
        for partner in partners:
            cluster = set()
            cluster.add(key)
            visited = set()
            visited.add(key)
            resCluster =  helper(partner, cluster, visited)
            if len(resCluster) > len(bestCluster):
                bestCluster = resCluster
    lst = list(bestCluster)
    lst.sort()

    print(",".join(lst))
