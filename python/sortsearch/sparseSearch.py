def sparseSearch(array, target):

    def binarySearch(array, left, right, target):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if array[mid] == "" and target != "":
            r = binarySearch(array, left, mid - 1, target)
            if r == -1:
                return binarySearch(array, mid + 1, right, target)
            else:
                return r
        elif array[mid] < target:
            return binarySearch(array, mid + 1, right, target)
        elif array[mid] > target:
            return binarySearch(array, left, mid - 1, target)
        else:
            return mid

    index = binarySearch(array, 0, len(array) - 1, target)

    return index

def main():
    x = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(sparseSearch(x, "ball"))
    print(sparseSearch(x, ""))

if __name__ == "__main__":
    main()
