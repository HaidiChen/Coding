from itertools import permutations

def string_to_number(operand, dic):
    s = ''
    for i in range(len(operand)):
        if i == 0 and dic[operand[i]] == 0:
            return 0
        s = s + str(dic[operand[i]])
    else:
        return int(s)

def go(string):
    letters = set(string)
    letters.remove('+')
    letters.remove('=')

    ops = separate(string)
    
    for p in permutations(range(10), len(letters)):
        dic = dict(zip(letters, p))
        res = 0
        num = 0
        nums = []
        for op in ops[:-1]:
            num = string_to_number(op, dic)
            res = res + num
            nums.append(num)
        result = string_to_number(ops[-1], dic)
        if res == result:
            for num in nums[:-1]:
                print(num)
                print('+')
            print(nums[-1])
            print('=')
            print(res)
            return 
    else:
        print('No result')
        return 

def separate(string):
    ops = []
    candidates = string.split('+')
    for x in candidates[:-1]:
        ops.append(x)
    lastOperand = candidates[-1].split('=')[0]
    result = candidates[-1].split('=')[1]
    ops.append(lastOperand)
    ops.append(result)

    return ops
