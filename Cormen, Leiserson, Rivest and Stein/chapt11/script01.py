# Functions

def division_method(k: int, m: int) -> int:
    return k % m

def multiplication_method(k: int, m: int, A=0.6180339887) -> int:
    return int(m * ((k * A) % 1))

# Execution

if __name__ == "__main__":
    print(division_method(100, 12))
    print(multiplication_method(123456, 16384))
