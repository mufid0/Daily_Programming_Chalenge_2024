def group_anagrams(strs):
    """
    Group all the strings that are anagrams of each other.

    Args:
        strs (list[str]): The array of strings.

    Returns:
        list[list[str]]: The grouped anagrams as a list of lists.
    """
    # Create a hashmap to store the anagrams
    anagrams = {}

    # Iterate over each string in the input array
    for word in strs:
        # Sort the characters in the string to create a key for the hashmap
        key = "".join(sorted(word))

        # If the key is not in the hashmap, add it with the current word as the value
        if key not in anagrams:
            anagrams[key] = [word]
        # If the key is already in the hashmap, append the current word to the value
        else:
            anagrams[key].append(word)

    # Return the values in the hashmap as a list of lists
    return list(anagrams.values())


def print_result(strs):
    """
    Print the grouped anagrams for the given input array.

    Args:
        strs (list[str]): The input array.
    """
    print("Input array:")
    print(strs)
    anagrams = group_anagrams(strs)
    print("Grouped anagrams:")
    print(anagrams)
    print()


# Test cases
test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["listen", "silent", "enlist", "inlets"],
    ["apple", "banana", "orange"],
    [""],
    ["alone"],
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
    ["abc", "bca", "cab", "xyz", "zyx", "yxz"],
    ["abc", "def", "ghi"]
]

expected_outputs = [
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
    [['listen', 'silent', 'enlist', 'inlets']],
    [['apple'], ['banana'], ['orange']],
    [['']],
    [['alone']],
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
    [['']],
    [['a']],
    [['abc', 'bca', 'cab'], ['xyz', 'zyx', 'yxz']],
    [['abc'], ['def'], ['ghi']]
]

for i, test_case in enumerate(test_cases):
    print("Test case", i+1)
    print_result(test_case)
    print("Expected output:", expected_outputs[i])
    print()