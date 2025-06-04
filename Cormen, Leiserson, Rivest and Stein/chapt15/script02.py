# Functions

def memoized_cut_rod(p, n):
    r = [float("-inf")] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float("-inf")
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i -1, r))
        r[n] = q
    return q


# Execution

if __name__ == "__main__":
    # Example 1
    prices = [1, 5, 8, 9]  # Prices for pieces size 1 to 4
    n = len(prices)
    print(memoized_cut_rod(prices, n))

    # Example 2
    prices = [1, 2, 3, 4, 5]
    n = len(prices)
    print(memoized_cut_rod(prices, n))

    # Example 3
    prices = [2, 5, 7, 8, 10, 17, 17]
    n = len(prices)
    print(memoized_cut_rod(prices, n))
