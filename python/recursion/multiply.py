def solution(a, b):
    values = {}
    def multiply(a, b):
        if a > b:
            a, b = b, a
        if a == 1:
            values[(a, b)] = b
            return b
        newA = a >> 1
        anotherA = a - newA
        if (newA, b) in values and (anotherA, b) in values:
            return values[(newA, b)] + values[(anotherA, b)]

        elif (newA, b) in values:
            tmp = multiply(anotherA, b)
            values[(anotherA, b)] = tmp

            return tmp + values[(newA, b)]

        elif (anotherA, b) in values:
            tmp = multiply(newA, b)
            values[(newA, b)] = tmp

            return tmp + values[(anotherA, b)]

        else:
            tmp1 = multiply(newA, b)
            tmp2 = multiply(anotherA, b)
            values[(newA, b)] = tmp1
            values[(anotherA, b)] = tmp2

            return tmp1 + tmp2

    result = multiply(a, b)
    return result

def main():
    for i in range(1,10):
        for j in range(i+1, 10):
            print('{} * {} == '.format(i, j),solution(j, i))

if __name__ == "__main__":
    main()
    
