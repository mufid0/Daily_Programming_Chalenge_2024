def find_missing_integer(arr):
    n = len(arr) + 1  # since one integer is missing
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(arr)
    missing_integer = total_sum - array_sum
    return missing_integer

# Test Case 1
arr = [1, 2, 4, 5]
missing_integer = find_missing_integer(arr)
print("Test Case 1: The missing integer is:", missing_integer)

# Test Case 2
arr = [2, 3, 4, 5]
missing_integer = find_missing_integer(arr)
print("Test Case 2: The missing integer is:", missing_integer)

# Test Case 3
arr = [1, 2, 3, 4]
missing_integer = find_missing_integer(arr)
print("Test Case 3: The missing integer is:", missing_integer)

# Test Case 4
arr = [1]
missing_integer = find_missing_integer(arr)
print("Test Case 4: The missing integer is:", missing_integer)

# Test Case 5
arr = list(range(1, 1000000))
missing_integer = find_missing_integer(arr)
print("Test Case 5: The missing integer is:", missing_integer)