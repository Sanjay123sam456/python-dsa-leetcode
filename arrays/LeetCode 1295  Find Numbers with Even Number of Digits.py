# LeetCode 1295 - Find Numbers with Even Number of Digits
# Topic: Arrays
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            digits = len(str(num))   # convert number to string and count length
            
            if digits % 2 == 0:
                count += 1
        
        return count
