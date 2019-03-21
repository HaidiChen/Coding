def me(arr):
    ''' this is not working correctly '''
    majority = arr[0]
    count = 1
    for x in arr[1 : ]:
        if count == 0:
            majority = x
            count = count + 1
        elif x == majority:
            count = count + 1
        else:
            count = count - 1
    print('majority element is: {0}'.format(majority))

def me2(arr):
    x = set(arr)
    for i in x:
        t = arr.count(i)
        if t >= (len(arr) // 2):
            print('majoritty element is: {0}'.format(i))
            break
    else:
        print('no result')
