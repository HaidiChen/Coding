def subset(array):
    if len(array) == 0:
        return [[]]
    first = array[:1]
    re = subset(array[1:])
    for r in re[:]:
        re.append(r + first)

    return re

def solution(array):
    subsets = []
    def subset(array):
        if len(array) == 0:
            subsets.append([])
            return
        first = array[:1]
        subset(array[1:])
        for e in subsets[:]:
            x = e.copy()
            x += first
            subsets.append(x)

    subset(array)
    return subsets

def main():
    print(solution([1,2,3]))

if __name__ == "__main__":
    main()
