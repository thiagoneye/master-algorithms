# Auxiliary Functions

def division(x: int, y: int) -> int:
    """
    Division.
    """
    q = 0
    r = 0
    
    if x != 0:
        while x > 0:
            print(f'\n{x} | {y} | {q} | {r}')
            
            q *= 2
            r *= 2
            
            if x % 2 != 0:
                r  += 1
            elif r >= y:
                q += 1
                r -= y
            
            x = int(x/2)
            y *= 2
    
    return (q, r)

# Execution

print(division(4, 2), '\n')
#print(division(252, 37), '\n')
print(division(81, 9), '\n')
#print(division(241, 31), '\n')
#print(division(109, 20), '\n')
