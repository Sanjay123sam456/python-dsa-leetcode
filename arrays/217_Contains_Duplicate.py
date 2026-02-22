# LeetCode 217 - Contains Duplicate
# Topic: Arrays, Hashing
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False