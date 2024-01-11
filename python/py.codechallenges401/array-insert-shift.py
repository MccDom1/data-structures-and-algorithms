def insertShiftArray(arr, value):
    # Calculate the middle index
    middle_index = len(arr) // 2


    # Shift elements to the right from middle_index to the end
    for i in range(len(arr) - 1, middle_index, -1):
        arr[i] = arr[i - 1]


    # Insert the value at the middle index
    arr[middle_index] = value

    return arr

