def ksubset(array, k):
    if k == len(array):
        return [array]
    if k == 0 or len(array) == 0:
        return [[]]

    first = array[:1]
    ss = ksubset(array[1:], k - 1)
    for i in range(len(ss)):
        ss[i] = ss[i] + first

    sss = ksubset(array[1:], k)
    return sss + ss

def main():
    x = []
    for i in range(200):
        x.append(i + 1)
    print(len(ksubset(x,3)))

if __name__ == "__main__":
    main()
