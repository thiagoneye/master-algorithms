# Functions

def modexp(x: int, y: int, N: int) -> int:
    """
    Modular Exponentiation.
    """
    if y == 0:
        return 1

    z = modexp(x, int(y/2), N)

    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * (z**2)) % N

# Execution

print(modexp(8, 4, 10))
