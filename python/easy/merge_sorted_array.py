def merge_sorted_array(a, b):
    j = 0
    i = 0
    m = len(a)
    n = len(b)
    while (i < len(a) and j < n):
        if a[i] < b[j]:
            i += 1
        else:
            a.insert(i, b[j])
            j += 1
            i += 1
    a += b[j:]
    return a

def msa(a, b):
    a += b
    return sorted(a)
