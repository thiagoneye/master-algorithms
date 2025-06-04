# Functions

def cut_rod(p, n):
    if n == 0:
        return 0

    r = float("-inf")

    for i in range(n):
        r = max(r, p[i] + cut_rod(p, n - i - 1))

    return r


# Execution

if __name__ == "__main__":
    # Example 1
    prices = [1, 5, 8, 9]  # Prices for pieces size 1 to 4
    n = len(prices)
    print(cut_rod(prices, n))

    # Example 2
    prices = [1, 2, 3, 4, 5]
    n = len(prices)
    print(cut_rod(prices, n))

    # Example 3
    prices = [2, 5, 7, 8, 10, 17, 17]
    n = len(prices)
    print(cut_rod(prices, n))
