# LeetCode 66 - Plus One
# Topic: Arrays
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9
        return [1] + digits