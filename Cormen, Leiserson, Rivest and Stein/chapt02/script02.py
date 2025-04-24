# Functions

def insertion_sort_descending(a: list):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i -= 1

        a[i+1] = key

# Execution

if __name__ == '__main__':
    a = [5, 2, 4, 6, 1, 3]
    insertion_sort_descending(a)
    print(a)
