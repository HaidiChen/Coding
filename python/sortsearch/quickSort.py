import random

def quickSort(seq):
    for i in range(len(seq)):
        j = random.randint(0, len(seq) - 1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp

    quickSortRecursively(seq, 0, len(seq))

def quickSortRecursively(seq, start, stop):
    if start >= stop - 1:
        return

    pivotIndex = partition(seq, start, stop)
    quickSortRecursively(seq, start, pivotIndex)
    quickSortRecursively(seq, pivotIndex + 1, stop)

def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1

    while i <= j:
        while i <= j and not pivot < seq[i]:
            i += 1
        
        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1

    seq[pivotIndex] = seq[j]
    seq[j] = pivot

    return j
