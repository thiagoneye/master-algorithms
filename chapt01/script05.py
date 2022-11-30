# Functions

def euclides(a: int, b: int) -> int:
    """
    Euclid's Algorithm for the Greatest Common Divisor.
    """
    if b == 0:
        return a

    return euclides(b, a % b)

# Execution

print(euclides(10, 5))
print(euclides(9876543, 49))
print(euclides(252, 105))
