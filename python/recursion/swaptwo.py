def swaptwo(string):
    if len(string) == 1:
        return string
    elif len(string) == 2:
        return string[1] + string[0]
    reststring = string[2:]
    return string[1] + string[0] + swaptwo(reststring)

def main():
    string = input('input your string:\n')
    print(swaptwo(string))

if __name__ == "__main__":
    main()
