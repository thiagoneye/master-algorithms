# Functions

def partition(A, low, high):
    x = A[high]
    pivot_idx = low - 1
    for j in range(low, high):
        if A[j] <= x:
            pivot_idx += 1
            A[pivot_idx], A[j] = A[j], A[pivot_idx]
    A[pivot_idx + 1], A[high] = A[high], A[pivot_idx + 1]
    return pivot_idx + 1


def quicksort(A, low, high):
    if low < high:
        q = partition(A, low, high)
        quicksort(A, low, q - 1)
        quicksort(A, q + 1, high)


# Execution

if __name__ == "__main__":
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    quicksort(A, 0, len(A) - 1)
    print(A)
