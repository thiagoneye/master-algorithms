# Functions

def merge(x: list, y: list) -> list:
    if len(x) == 0:
        return y

    if len(y) == 0:
        return x

    if x[0] <= y[0]:
        return [x[0]] + merge(x[1:], y)
    else:
        return [y[0]] + merge(x, y[1:])

# Execution

if __name__ == '__main__':
    x = [1, 3, 5, 7, 9]
    y = [0, 2, 4, 6, 8]

    print(merge(x,y))
