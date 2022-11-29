# Auxiliary Functions

def multiplication(x, y):
    """ multiplication ala francais"""
    # Base Case
    if y == 0:
        return 0

    # Recursive Case
    z = multiplication(x, int(y / 2))

    if y % 2 == 0:
        return 2 * z
    else:
        return x + 2 * z

# Execution

print(multiplication(10, 10))
print(multiplication(81, 102))
