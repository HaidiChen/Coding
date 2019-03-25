def mco(arr):
    n = len(arr)
    count = 0
    m = 0
    for x in arr:
        if x == 0:
            m = max(count, m)
            count = 0
        else:
            count = count + 1
    print(m)
