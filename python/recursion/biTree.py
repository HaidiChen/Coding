def bt(n):
    if n == 0:
        return [None]
    result = []
    for x in range(n):
        lt = bt(x)
        rt = bt(n - 1 - x)
        result +=[(0, l, r) for l in lt for r in rt]
    return result

def main():
    r = bt(4)
    for i in r:
        print(i)

if __name__ == "__main__":
    main()
