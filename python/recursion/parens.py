def parens(n):
    if n == 0:
        return [""]
    results = []
    ps = parens(n - 1)
    for p in ps:
        r = applyRules(p)
        results += r

    return results

def applyRules(p):
    results = set()

    p1 = p + "()"
    p2 = "()" + p
    p3 = "(" + p + ")"
    results.add(p1)
    results.add(p2)
    results.add(p3)
    
    return results

def main():
    print(parens(2))
    print(parens(3))

if __name__ == "__main__":
    main()
