# Functions

def bubblesort(A: list):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

# Execution

if __name__ == '__main__':
    A = [9, 2, 4, 0, 9, 7, 1, 4, 2, 3, 3, 1]
    bubblesort(A)
    print(A)
