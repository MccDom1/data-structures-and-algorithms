def binary_search(arr, key):
    """
    Perform binary search on a sorted array to find the index of the search key.

    Parameters:
    - arr: List[int] - A sorted array.
    - key: int - The search key.

    Returns:
    - int: The index of the array's element equal to the search key, or -1 if not found.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == key:
            return mid  # Key found, return the index
        elif mid_value < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Key not found in the array

# Test cases
print(binary_search([4, 8, 15, 16, 23, 42], 15))    # Output: 2
print(binary_search([-131, -82, 0, 27, 42, 68, 179], 42))  # Output: 4
print(binary_search([11, 22, 33, 44, 55, 66, 77], 90))    # Output: -1
print(binary_search([1, 2, 3, 5, 6, 7], 4))               # Output: -1
