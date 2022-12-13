# Imports

from random import choice

# Functions

def selection(s: list, k: int) -> int:
    v = choice(s)

    sl = [x for x in s if x < v]
    sv = [x for x in s if x == v]
    sr = [x for x in s if x > v]

    if k <= len(sl):
        return selection(sl, k)
    elif k <= len(sl) + len(sv):
        return v
    else:
        return selection(sr, k-len(sl)-len(sv))

# Execution

if __name__ == '__main__':
    s = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0, 99, 42, 60, 1, 254, 10, 12, 14]
    k = int(len(s)/2)
    median = selection(s, k)

    print(median)
