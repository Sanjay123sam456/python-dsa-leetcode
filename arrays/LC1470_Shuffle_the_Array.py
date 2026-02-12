# LeetCode 1470 - Shuffle the Array
# Topic: Arrays
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans
