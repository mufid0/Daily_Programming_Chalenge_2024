def trap_water(height):
    """
    Calculate the total amount of water that can be trapped in the histogram-like structure.

    Args:
        height (list): A list of non-negative integers representing the height of each bar in the histogram.

    Returns:
        int: The total amount of water that can be trapped.
    """
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    total_water = 0

    # Calculate left_max
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i-1])

    # Calculate right_max
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i+1])

    # Calculate total_water
    for i in range(n):
        total_water += max(0, min(left_max[i], right_max[i]) - height[i])

    return total_water


def print_result(height):
    """
    Print the total amount of water that can be trapped for the given input array.

    Args:
        height (list): A list of non-negative integers representing the height of each bar in the histogram.
    """
    print("Input array:")
    print(height)
    total_water = trap_water(height)
    print("Total amount of water that can be trapped:", total_water)


# Test cases
test_cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
    [1, 1, 1],
    [5],
    [2, 0, 2]
]

expected_outputs = [6, 9, 0, 0, 2]

for i, test_case in enumerate(test_cases):
    print("Test case", i+1)
    print_result(test_case)
    print("Expected output:", expected_outputs[i])
    print()