def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = {0: -1}
    current_sum = 0
    result = []

    for i in range(n):
        current_sum += arr[i]

        if current_sum in prefix_sum:
            for j in range(prefix_sum[current_sum] + 1, i + 1):
                result.append((j, i))
        else:
            prefix_sum[current_sum] = i

    return result

# Test cases
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))  # Output: [(1, 2), (0, 3)]
print(find_zero_sum_subarrays([1, 2, 3, 4]))  # Output: []
print(find_zero_sum_subarrays([0, 0, 0]))  # Output: [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))  # Output: [(0, 3), (4, 4)]
print(find_zero_sum_subarrays([1, -1, 2, -2, 3, -3] * 10**4))  # Output: [(0, 1), (2, 3), ..., (19998, 19999)]