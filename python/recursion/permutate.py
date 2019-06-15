def perm(array):
    if len(array) == 1:
        return [array]
    first = array[0]
    permList = perm(array[1:])
    results = []
    for p in permList:
        for i in range(0, len(p) + 1):
            pp = p.copy()
            pp.insert(i, first)
            results.append(pp)

    return results
