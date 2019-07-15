def compress(string):
    if len(string) == 0:
        return string
    arr = list(string)
    lastIdx = len(arr) - 1
    count = 1
    prev = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if lastIdx < 0:
            return string
        if arr[i] != prev:
            arr[lastIdx] = count
            arr[lastIdx - 1] = prev
            count = 1
            prev = arr[i]
            lastIdx -= 2
        else:
            count += 1

    arr[lastIdx] = count
    arr[lastIdx - 1] = prev
    lastIdx -= 2

    del arr[:lastIdx + 1]
    return arr

def main():
    ex = "aabcccccaaa"
    ex2 = "AAAbacdddfeeEE"
    print(compress(ex))
    print(compress(ex2))

if __name__ == '__main__':
    main()
