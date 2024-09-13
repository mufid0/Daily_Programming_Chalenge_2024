def find_leaders(input_array):
    """
    Find all leaders in the input array.
    A leader is an element that is greater than all elements to its right.
    """
    leader_elements = []
    max_so_far = float('-inf')

    # Iterate through the array from right to left
    for i in range(len(input_array) - 1, -1, -1):
        # Check if the current element is a leader
        if input_array[i] > max_so_far:
            leader_elements.append(input_array[i])
            max_so_far = input_array[i]

    # Return the leaders in the original order
    return leader_elements[::-1]
# Example usage:
arr = [16, 17, 4, 3, 5, 2]
leaders = find_leaders(arr)
print("Leaders in the Example array:", leaders)

# Test cases
test_cases = [
    ([1, 2, 3, 4, 0], [4, 0]),
    ([7, 10, 4, 10, 6, 5, 2], [10, 6, 5, 2]),
    ([5], [5]),
    ([100, 50, 20, 10], [100, 50, 20, 10]),
    (list(range(1, 1000001)), [1000000])
]

for test_case in test_cases:
    input_array, expected_output = test_case
    leaders = find_leaders(input_array)
    print(f"Input: {input_array}, Output: {leaders}, Expected: {expected_output}")
    assert leaders == expected_output