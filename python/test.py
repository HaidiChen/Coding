name = "Bruce"
age = 22
salary = 2222.22

#print(name)
#print(age)
#print(salary)

list = ["abc", 23, 50.4, "jads"]
tuple = ("abc", 2, 23.23)

a = 20
b = 20

if (a is b):
    print("Line 1 - a and b have same identity")
else :
    print("Line 1 - a and b not have same identity")

if (id(a) == id(b)):
    print("Line 2 - a and b have same identity")
else :
    print("Line 2 - a and b not have same identity")

if (a is b):
    print("Line 1 - a and b have same identity")
else :
    print("LIne 2 - a and b not have same identity")

if (a is not b):
    print("Line 2 - a and b not have same identity")
else :
    print("Line 2 - a and b have same identity")

def max_subarray2(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    startOld = start = end = 0
    for i, x in enumerate(A[1:], 1):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            start = i + 1
        elif max_ending_here == max_so_far:
            startOld = start
            end = i
    return (max_so_far, startOld, end)

ex = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ex2 = [-2, 1, -3, 4, -1, 2, 1, -8, 7]

def test():
    print(max_subarray(ex))
    print(max_subarray(ex2))

def test2():
    print(max_subarray2(ex))

def plus_one(digits):
    digits.insert(0, 0)
    n = len(digits)
    if digits[n - 1] < 9:
        digits[n - 1] += 1
    else:
        digits[n - 1] = 0
        digits[:n - 1] = plus_one(digits[1:n - 1])
    if digits[0] == 0:
        del digits[0]
    return digits

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
