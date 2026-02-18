# LeetCode 1672 - Richest Customer Wealth
# Topic: Arrays
# Difficulty: Easy
# Time Complexity: O(m * n)
# Space Complexity: O(1)

class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for i in range(len(accounts)):
            current_sum = 0
            
            for j in range(len(accounts[i])):
                current_sum += accounts[i][j]
            
            if current_sum > max_wealth:
                max_wealth = current_sum
        
        return max_wealth
