def hanoi(n, p1, p2, p3):
    if n == 1:
        move(p1, p2)
        return
    hanoi(n - 1, p1, p3, p2)
    move(p1, p2)
    hanoi(n - 1, p3, p2, p1)

def move(x, y):
    print('from {} to {}'.format(x, y))

