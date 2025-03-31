# Functions

def linear_search(a: list, v: int):
    for idx, value in enumerate(a):
        if v == value:
            return idx
        
    return None

# Execution

if __name__ == "__main__":
    print(linear_search([6, 4, 2, 8, 9, 1, 3, 7, 5], 1))
