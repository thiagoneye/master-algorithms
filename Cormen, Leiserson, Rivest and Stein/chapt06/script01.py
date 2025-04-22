def parent(i: int) -> int:
    return (i - 1)//2

def left(i: int) -> int:
    return 2*i + 1

def right(i: int) -> int:
    return 2*i + 2

def max_heapify(A: list, n: int, i: int):
    l = left(i)
    r = right(i)
    largest = i

    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)

def build_max_heap(A: list):
    n = len(A)
    for idx in range(n//2 - 1, -1, -1):
        max_heapify(A, n, idx)

def heapsort(A: list) -> list:
    build_max_heap(A)
    
    n = len(A)
    for idx in range(n-1, 0, -1):
        A[0], A[idx] = A[idx], A[0]
        max_heapify(A, idx, 0)

# Priority Queues

def heap_maximum(A: list) -> int:
    return A[0]

def heap_extract_max(A: list) -> int:
    n = len(A)
    if n < 1:
        raise IndexError("Heap underflow!")
    
    maximum = A[0]
    A[0] = A[-1]
    A.pop()
    max_heapify(A, len(A), 0)
    
    return maximum

def heap_increase_key(A: list, i: int, key: int):
    if key < A[i]:
        raise ValueError("The new key is smaller than current key.")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def max_heap_insert(A: list, key: int):
    A.append(float('-inf'))
    heap_increase_key(A, len(A)-1, key)

if __name__ == "__main__":
    A = [16, 4,  10, 14, 7, 9, 3, 2, 8, 1]
    
    heapsort(A)
    print(A)

    build_max_heap(A)
    print(A)

    # Priority Queues

    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(A)

    print("Max:", heap_maximum(A))
    print("Extracted Max:", heap_extract_max(A))
    print("After extraction:", A)

    max_heap_insert(A, 20)
    print("After inserting 20:", A)

    heap_increase_key(A, 3, 22)
    print("After increasing key at index 3 to 22:", A)
