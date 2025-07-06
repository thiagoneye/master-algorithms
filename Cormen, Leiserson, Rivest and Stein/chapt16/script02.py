# Functions


def greedy_activity_selector(s: list, f: list) -> list:
    n = len(s)
    c = [0]
    k = 0

    for m in range(1, n):
        if s[m] >= f[k]:
            c.append(m)
            k = m

    return c


# Execution

if __name__ == "__main__":
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    c = greedy_activity_selector(s, f)

    print("Activities:")
    print(f"Start: {s}")
    print(f"End: {f}")
    print(f"\nSelected activity indices (original order): {c}")

    activities = [(s[idx], f[idx]) for idx in c]
    print(f"Selected activities (start, end): {activities}")
