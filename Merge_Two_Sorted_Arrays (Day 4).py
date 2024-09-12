def reorder_arrays(arr1, arr2):
    merged_arr = arr1 + arr2
    merged_arr.sort()
    mid = len(merged_arr) // 2
    arr1 = merged_arr[:mid]
    arr2 = merged_arr[mid:]
    return arr1, arr2

# Test Case 1
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
arr1, arr2 = reorder_arrays(arr1, arr2)
print("arr1 (reordered based on merged array):", arr1)
print("arr2 (reordered based on merged array):", arr2)

# Test Case 2
arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
arr1, arr2 = reorder_arrays(arr1, arr2)
print("arr1 (reordered based on merged array):", arr1)
print("arr2 (reordered based on merged array):", arr2)

# Test Case 3
arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
arr1, arr2 = reorder_arrays(arr1, arr2)
print("arr1 (reordered based on merged array):", arr1)
print("arr2 (reordered based on merged array):", arr2)

# Test Case 4
arr1 = [1]
arr2 = [2]
arr1, arr2 = reorder_arrays(arr1, arr2)
print("arr1 (reordered based on merged array):", arr1)
print("arr2 (reordered based on merged array):", arr2)

# Test Case 5
arr1 = list(range(1, 50001))
arr2 = list(range(50001, 100001))
arr1, arr2 = reorder_arrays(arr1, arr2)
print("arr1 (reordered based on merged array):", arr1)
print("arr2 (reordered based on merged array):", arr2)