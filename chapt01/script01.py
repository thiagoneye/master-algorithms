# Functions

def multiplication(x: int, y: int) -> int:
    """
    Multiplication à la Français.
    """
    if y == 0:
        z = 0
    else:
        z = list()

        while x > 0:
            if x % 2 != 0:
                z.append(y)

            x = int(x/2)
            y *= 2

    z = sum(z)

    return z

# Execution

print(multiplication(25, 37), '\n')
print(multiplication(81, 102), '\n')
print(multiplication(24, 31), '\n')
print(multiplication(10, 20), '\n')
