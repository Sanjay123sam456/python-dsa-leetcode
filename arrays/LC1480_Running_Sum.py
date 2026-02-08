# LeetCode 1480 - Running Sum of 1D Array
# Difficulty: Easy
# Topic: Arrays
#
# Approach:
# Traverse the array from left to right.
# Keep a cumulative sum and store it after each step.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def runningSum(self, nums):
        result = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            result.append(total)

        return result
