# Imports

import random
from collections import Counter

# Functions

def primality_test(N: int) -> bool:
    """
    Primality Test.
    """
    a = random.randint(0, N-1)

    if (a ** (N - 1) - 1) % N == 0:
        return True

    return False

# Execution

if __name__ == '__main__':
    results = list()

    for _ in range(100):
        results.append(primality_test(10))

    print(Counter(results))

    for _ in range(100):
        results.append(primality_test(17))

    print(Counter(results))
