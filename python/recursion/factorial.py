def fact(n):
    # base case
    if n == 0:
        return 1

    # recursive case
    return n * fact(n - 1)

def main():
    n = int(input('Input your N, and I will give you the factorial:\n'))
    print('factorial of {} is'.format(n), fact(n))

if __name__ == "__main__":
    main()
