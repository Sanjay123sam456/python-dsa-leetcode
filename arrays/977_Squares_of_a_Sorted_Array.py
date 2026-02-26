class Solution:
    def sortedSquares(self, nums):
        result = []

        for x in nums:
            result.append(x * x)

        result.sort()
        return result
