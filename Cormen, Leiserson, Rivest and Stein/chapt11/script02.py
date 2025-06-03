# Imports

from script01 import division_method

# Classes

class ChainedHash:
    def __init__(self, m: int, function=division_method):
        self._m = m
        self.T = [[] for _ in range(self._m)]
        self._function = function

    def insert(self, x):
        idx = self._function(x, self._m)
        self.T[idx].append(x)

    def search(self, k):
        i = self._function(k, self._m)
        j = None

        for key, value in enumerate(self.T[i]):
            if k == value:
                j = key

        return i, j

    def delete(self, x):
        i, j = self.search(x)

        if j is not None:
            del self.T[i][j]


# Executions

if __name__ == "__main__":
    # Create a New Hash Table
    hash_table = ChainedHash(9)

    # Insertion
    hash_table.insert(5)
    hash_table.insert(28)
    hash_table.insert(19)
    hash_table.insert(15)
    hash_table.insert(20)
    hash_table.insert(33)
    hash_table.insert(12)
    hash_table.insert(17)
    hash_table.insert(10)

    # Print
    print(hash_table.T)

    # Search
    i, j = hash_table.search(33)
    print(f"i: {i} and j: {j}")

    # Delete
    hash_table.delete(12)

    # Print
    print(hash_table.T)
