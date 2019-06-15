def decompose(string):
    def dp(offset, partial_partition):
        if offset == len(string):
            result.append(list(partial_partition))
            return
        
        for i in range(offset + 1, len(string) + 1):
            prefix = string[offset:i]
            if prefix == prefix[::-1]:
                dp(i, partial_partition + [prefix])

    result = []
    dp(0, [])
    return result

def main():
    string = '61116'
    t = decompose(string)
    print(t)


if __name__ == "__main__":
    main()
