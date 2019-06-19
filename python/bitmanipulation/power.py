def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        if power & 1:
            result *= x

        x, power = x * x, power >> 1

    return result

def main():
    result = power(1.5, 4)
    print(result)


if __name__ == '__main__':
    main()
