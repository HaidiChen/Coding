def length(string):
    if string == "":
        return 0
    reststring = string[1:]
    return 1 + length(reststring)

def main():
    string = input('enter whatever string you want '
            + 'and length will be poped out to you:\n')
    print('length of ' + string + ' is ', length(string))

if __name__ == "__main__":
    main()
