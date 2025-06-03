# Functions

def counting_sort(A: list) -> list:
    k = max(A)
    B = [None] * len(A)
    C = [0] * (k + 1)

    for value in A:
        C[value] += 1

    # Cumulative Sum
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        value = A[j]
        idx = C[value] - 1
        B[idx] = value
        C[value] -= 1

    return B


# Execution

if __name__ == "__main__":
    print(counting_sort([7, 1, 0, 2, 6, 3, 4, 4, 4, 5, 1, 6]))
