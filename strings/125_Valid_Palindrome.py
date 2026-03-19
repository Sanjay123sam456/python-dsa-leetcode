# LeetCode 125 - Valid Palindrome
# Topic: Strings
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s):
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        return cleaned == cleaned[::-1]