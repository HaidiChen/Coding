def combination(arr, target):
    comb = []
    result = []
    arr.sort()
    find(comb, result, arr, target, 0)
    print(result)

def find(comb, result, arr, target, k):
    if target < 0:
        return
    elif target == 0:
        result.append(comb[:])
    else:
        for i in range(k, len(arr)):
            if i > k and arr[i] == arr[i - 1]:
                continue
            comb.append(arr[i])
            find(comb, result, arr, target - arr[i], i + 1)
            del comb[-1]
