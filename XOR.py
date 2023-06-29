def subsetXORSum(nums):
    def generateSubsets(idx, curr_xor):
        nonlocal total_xor

        # Base case: reached the end of nums
        if idx == len(nums):
            total_xor += curr_xor
            return

        # Include nums[idx] in the current subset
        generateSubsets(idx + 1, curr_xor ^ nums[idx])

        # Exclude nums[idx] from the current subset
        generateSubsets(idx + 1, curr_xor)

    total_xor = 0
    generateSubsets(0, 0)
    return total_xor

# Test case 1
nums1 = [1, 3]
print("Sum of XOR Totals:", subsetXORSum(nums1))  # Output: 6

# Test case 2
nums2 = [5, 1, 6]
print("Sum of XOR Totals:", subsetXORSum(nums2))  # Output: 28
