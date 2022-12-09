# Imports

from script01 import merge

# Functions

def mergesort(a: list) -> list:
    n = len(a)

    if n > 1:
        return merge(mergesort(a[:int(n/2)]), mergesort(a[int(n/2):]))
    else:
        return a

# Execution

if __name__ == '__main__':
    a = [9, 2, 4, 0, 9, 7, 1, 4, 2, 3, 3, 1]

    print(mergesort(a))
