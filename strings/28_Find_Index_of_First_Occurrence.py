# LeetCode 28 - Find Index of First Occurrence in a String
# Topic: Strings
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Using built-in function
        return haystack.find(needle)


# Example usage (for testing locally)
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.strStr("sadbutsad", "sad"))   # Output: 0
    print(sol.strStr("leetcode", "leeto"))  # Output: -1