# Functions


def recursive_activity_selector(s: list, f: list, k: int, n: int) -> list:
    """
    Recursive activity selector algorithm.
    Selects the maximum number of mutually compatible activities.

    Parameters:
    s -- List of start times (indexed from 0).
    f -- List of finish times (must be sorted in increasing order).
    k -- Index of the last selected activity.
    n -- Total number of activities.

    Returns:
    A list (c) of indices representing the selected activities.
    """
    m = k + 1

    while m < n and s[m] < f[k] if k != -1 else False:
        m += 1

    if m < n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def sort_activities(s: list, f: list):
    """
    Sorts activities by their finish times in ascending order.
    This function takes two lists: start times and finish times of a set of activities.
    It returns the start and finish times sorted according to the increasing order
    of the finish times, which is useful for greedy algorithms such as the activity selection problem.

    Parameters:
    s -- A list of activity start times.
    f -- A list of activity finish times, corresponding to the start times.

    Returns:
    Two tuples: (s_sorted, f_sorted), where each is the sequence of start and finish times sorted by finish time.
    """
    activities = sorted(enumerate(zip(s, f)), key=lambda x: x[1][1])
    _, sorted_activities = zip(*activities)
    s_sorted, f_sorted = zip(*sorted_activities)

    return s_sorted, f_sorted


# Execution

if __name__ == "__main__":
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    n = len(s)
    c = recursive_activity_selector(s, f, -1, n)

    print("Activities:")
    print(f"Start: {s}")
    print(f"End: {f}")
    print(f"\nSelected activity indices (original order): {c}")

    activities = [(s[idx], f[idx]) for idx in c]
    print(f"Selected activities (start, end): {activities}")
