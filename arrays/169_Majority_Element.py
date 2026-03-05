# LeetCode 169 - Majority Element
# Topic: Arrays, Hashing
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums):
        count = {}
        n = len(nums)
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num