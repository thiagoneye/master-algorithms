# Functions

def extended_euclid(a: int, b: int) -> int:
    """
    Extended Euclid.
    a > b
    """
    if b == 0:
        return (1, 0, a)

    x, y, d = extended_euclid(b, (a % b))

    return (y, x - int(a/b)*y, d)

# Execution

print(extended_euclid(120, 23))
