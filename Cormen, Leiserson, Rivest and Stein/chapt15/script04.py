# Functions


def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)

    for j in range(1, n + 1):
        q = float("-inf")

        for i in range(j):
            if q < (p[i] + r[j - i - 1]):
                q = p[i] + r[j - i - 1]
                s[j] = i + 1
        r[j] = q

    return r, s


def print_cut_rod_solutions(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)

    print(f"p:{p}")
    print(f"r:{r}")
    print(f"s:{s}")

    while n > 0:
        print(s[n], end=" ")
        n -= s[n]


# Execution

if __name__ == "__main__":
    # Example 1
    prices = [1, 5, 8, 9]  # Prices for pieces size 1 to 4
    n = len(prices)
    print_cut_rod_solutions(prices, n)
    print("\n")

    # Example 2
    prices = [1, 2, 3, 4, 5]
    n = len(prices)
    print_cut_rod_solutions(prices, n)
    print("\n")

    # Example 3
    prices = [2, 5, 7, 8, 10, 17, 17]
    n = len(prices)
    print_cut_rod_solutions(prices, n)
    print("\n")

    # Example 4
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(prices)
    print_cut_rod_solutions(prices, n)
    print("\n")
