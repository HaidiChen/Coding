def pascal_triangle(rowNum):
    pre_row = row = []
    for i in range(rowNum):
        row.insert(0, 1)
        for j in range(1, i):
            row.append(pre_row[j - 1] + pre_row[j])
        if i != 0:
            row.append(1)
        pre_row = row
        print(row)
        row = []
