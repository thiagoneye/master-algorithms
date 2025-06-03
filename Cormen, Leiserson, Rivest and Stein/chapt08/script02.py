# Functions

def bucket_sort(A: list) -> list:
    n = len(A)
    B = [[] for _ in range(n)]
    C = []

    for value in A:
        idx = int(n * value)
        B[idx].append(value)

    for idx in range(n):
        B[idx] = sorted(B[idx])

    for i in B:
        for j in i:
            C.append(j)

    return C


# Execution

if __name__ == "__main__":
    print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))
