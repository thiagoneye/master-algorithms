# Imports

from script01 import division_method

# Functions

def chained_hash(m: int) -> list:
    T = [[] for _ in range(m)]
    return T


def chained_hash_insert(T, x, function=division_method):
    m = len(T)
    idx = division_method(x, m)
    T[idx].append(x)


def chained_hash_search(T, k, function=division_method):
    m = len(T)
    i = division_method(k, m)
    j = None

    for key, value in enumerate(T[i]):
        if k == value:
            j = key

    return i, j


def chained_hash_delete(T, x, function=division_method):
    i, j = chained_hash_search(T, x)

    if j is not None:
        del T[i][j]


# Executions

if __name__ == "__main__":
    # Create a New Hash Table
    T = chained_hash(9)

    # Insertion
    chained_hash_insert(T, 5)
    chained_hash_insert(T, 28)
    chained_hash_insert(T, 19)
    chained_hash_insert(T, 15)
    chained_hash_insert(T, 20)
    chained_hash_insert(T, 33)
    chained_hash_insert(T, 12)
    chained_hash_insert(T, 17)
    chained_hash_insert(T, 10)

    # Print
    print(T)

    # Search
    i, j = chained_hash_search(T, 33)
    print(f"i: {i} and j: {j}")

    # Delete
    chained_hash_delete(T, 12)

    # Print
    print(T)
