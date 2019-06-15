def solution(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    result = set()
    r = solution(n - 1)
    for c in r:
        newc = '()' + c
        result.add(newc)
        newc = '(' + c + ')'
        result.add(newc)
        newc = c + '()'
        result.add(newc)

    return result

def main():
    print(solution(3))
    print(solution2(3))



def solution2(n):
    result = []
    def parens(left, right, string):
        if left > right or left < 0:
            return
        if left == 0 and right == 0:
            result.append(string)
        else:
            tmp = string[:]
            tmp = tmp + '('
            parens(left - 1, right, tmp)

            tmp = string[:]
            tmp = tmp + ')'
            parens(left, right - 1,tmp)

    string = str()
    parens(n, n, string)
    return result

if __name__ == "__main__":
    main()

