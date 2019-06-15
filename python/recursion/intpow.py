def intpow(x, n):
    if n == 0:
        return 1
    return intpow(x, n - 1) * x

def main():
    x = input('enter the X:\n')
    x = int(x)
    n = input('enter the n:\n')
    n = int(n)

    print('{} ^ {} ='.format(x, n), intpow(x, n))

if __name__ == "__main__":
    main()
