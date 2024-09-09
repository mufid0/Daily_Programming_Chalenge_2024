def sort_array(arr):
    """
    Sorts an array of 0s, 1s, and 2s in increasing order in linear time.

    Args:
        arr (list): The input array consisting only of 0s, 1s, and 2s.

    Returns:  
        list: The sorted array.
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid]
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            # Swap arr[mid] and arr[high]
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage:
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_array(arr))  # Output: [0, 0, 0, 1, 1, 1, 2, 2]
