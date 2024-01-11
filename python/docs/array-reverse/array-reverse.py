# Iterative approach
def reverseArrayIterative(arr):
    length = len(arr)
    reversed_arr = [0] * length  # Initialize a new array of the same length

    for i in range(length):
        reversed_arr[length - 1 - i] = arr[i]

    return reversed_arr

# Recursive approach
def reverseArrayRecursive(arr, index=None):
    if index is None:
        index = len(arr) - 1

    if index < 0:
        return []
    else:
        return [arr[index]] + reverseArrayRecursive(arr, index - 1)

# Example usage
input_array = [1, 2, 3, 4, 5, 6]

# Test the iterative approach
iterative_result = reverseArrayIterative(input_array)
print("Iterative Result:", iterative_result)

# Test the recursive approach
recursive_result = reverseArrayRecursive(input_array)
print("Recursive Result:", recursive_result)
