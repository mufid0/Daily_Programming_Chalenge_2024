def longest_common_prefix(strs):
    """
    Find the longest common prefix among an array of strings.

    Args:
        strs (list[str]): The array of strings.

    Returns:
        str: The longest common prefix.
    """
    # If the array is empty, return an empty string
    if not strs:
        return ""

    # Initialize the prefix as an empty string
    prefix = ""

    # Iterate over the characters in the first string
    for chars in zip(*strs):
        # Convert the characters to a set
        char_set = set(chars)

        # If the set contains more than one character, break the loop
        if len(char_set) > 1:
            break

        # Add the common character to the prefix
        prefix += char_set.pop()

    return prefix


def print_result(strs):
    """
    Print the longest common prefix for the given input array.

    Args:
        strs (list[str]): The input array.
    """
    print("Input array:")
    print(strs)
    prefix = longest_common_prefix(strs)
    print("Longest common prefix:")
    print(prefix)
    print()


# Test cases
test_cases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["apple", "ape", "april"],
    [""],
    ["alone"]
]

expected_outputs = [
    "fl",
    "",
    "ap",
    "",
    "alone"
]

for i, test_case in enumerate(test_cases):
    print("Test case", i+1)
    print_result(test_case)
    print("Expected output:", expected_outputs[i])
    print()