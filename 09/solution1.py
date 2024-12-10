with open('input.txt') as file:
    ret = 0
    arr = []
    for line in file.readlines():
        isFree = False
        id_counter = 0
        # Build the array
        for c in line:
            i = int(c)
            
            for _ in range(i):
                if isFree:
                    arr.append(".")
                else:
                    arr.append(id_counter)
            if isFree:
                isFree = False
            else:
                isFree = True
                id_counter += 1
    start, end = 0, len(arr) - 1
    while start <= end:
        if arr[start] == ".":
            while arr[end] == ".":
                end -= 1
            if end < start:
                break
            arr[start] = arr[end]
            end -= 1
        ret += arr[start] * start
        start += 1
    print(ret)