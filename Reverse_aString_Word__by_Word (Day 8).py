def reverse_words(s):
    """
    Reverse the order of words in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with the order of words reversed.
    """
    # Split the string into words
    words = s.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_s = ' '.join(reversed_words)

    return reversed_s


def print_result(s):
    """
    Print the reversed string for the given input string.

    Args:
        s (str): The input string.
    """
    print("Input string:")
    print(s)
    reversed_s = reverse_words(s)
    print("Reversed string:")
    print(reversed_s)


# Test cases
test_cases = [
    "the sky is blue",
    "  hello world  ",
    "a good   example",
    "    ",
    "word"
]

expected_outputs = [
    "blue is sky the",
    "world hello",
    "example good a",
    "",
    "word"
]

for i, test_case in enumerate(test_cases):
    print("Test case", i+1)
    print_result(test_case)
    print("Expected output:", expected_outputs[i])
    print()