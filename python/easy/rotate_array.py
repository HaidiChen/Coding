def ra(arr, k):
    n = len(arr)
    arr_1 = arr[ : n - k]
    arr_2 = arr[n - k : ]
    arr = arr_2 + arr_1
    print(arr)

def ra2(arr, k):
    n = len(arr)
    for i in range(n - k, n):
        t = i
        for j in range(n - k):
            temp = arr[t]
            arr[t] = arr[t - 1]
            arr[t - 1] = temp
            t = t - 1
    print(arr)

def ra3(arr, k):
    n = len(arr)
    temp_arr = arr[n - k : ]
    temp_arr.reverse()
    for x in temp_arr:
        arr.insert(0, x)
        arr.pop()
    print(arr)
