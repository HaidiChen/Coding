def triangle(k):
    row = pre_row = []
    n = k + 1
    for i in range(n):
        row.insert(0, 1)
        for j in range(1, i):
            row.insert(j, pre_row[j - 1] + pre_row[j])
        if i != 0:
            row.insert(i, 1)
        pre_row = row
        if i == k:
            break
        row = []
    print(row) 


