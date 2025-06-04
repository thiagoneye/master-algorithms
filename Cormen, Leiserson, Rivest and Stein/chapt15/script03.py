# Functions


def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)

    for j in range(1, n + 1):
        q = float("-inf")

        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q

    return r[n]


# Execution

if __name__ == "__main__":
    # Example 1
    prices = [1, 5, 8, 9]  # Prices for pieces size 1 to 4
    n = len(prices)
    print(bottom_up_cut_rod(prices, n))

    # Example 2
    prices = [1, 2, 3, 4, 5]
    n = len(prices)
    print(bottom_up_cut_rod(prices, n))

    # Example 3
    prices = [2, 5, 7, 8, 10, 17, 17]
    n = len(prices)
    print(bottom_up_cut_rod(prices, n))
