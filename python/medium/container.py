def container(arr):
    n = len(arr)
    i = 0
    j = n - 1
    m = 0
    while i != j:
        height = min(arr[i], arr[j])
        width = j - i
        m = max(m, height * width)
        if arr[i] > arr[j]:
            j = j - 1
        else:
            i = i + 1
    print(m)

def container2(arr):
    n = len(arr)
    m = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            height = min(arr[i], arr[j])
            width = j - i
            m = max(height * width, m)
    print(m)
