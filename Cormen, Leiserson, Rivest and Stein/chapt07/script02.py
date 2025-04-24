# Imports

import random
from script01 import partition

# Functions

def randomized_partition(A, low, high):
    i = random.randint(low, high)
    A[low], A[i] = A[i], A[low]
    
    return partition(A, low, high)

def randomized_quicksort(A, low, high):
    if low < high:
        q = randomized_partition(A, low, high)
        randomized_quicksort(A, low, q-1)
        randomized_quicksort(A, q+1, high)

# Execution

if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    randomized_quicksort(A, 0, len(A)-1)
    print(A)
