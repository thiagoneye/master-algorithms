# Functions

def find_max_crossing_subarray(A: list, low: int, mid: int, high: int) -> tuple:
    left_sum = float("-inf")
    sum_value = 0
    max_left = mid
    
    for i in range(mid, low-1, -1):
        sum_value += A[i]
        if sum_value > left_sum:
            left_sum = sum_value
            max_left = i
    
    right_sum = float("-inf")
    sum_value = 0
    max_right = mid + 1

    for j in range(mid+1, high+1):
        sum_value += A[j]
        if sum_value > right_sum:
            right_sum = sum_value
            max_right = 1
    
    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(A: list, low: int, high: int) -> tuple:
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low+high)/2)
        
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# Execution

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    low, high, max_sum = find_maximum_subarray(A, 0, len(A) - 1)
    print(f"Subarray máximo vai de {low} até {high} com soma = {max_sum}")
