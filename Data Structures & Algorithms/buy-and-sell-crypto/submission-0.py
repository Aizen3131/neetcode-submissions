class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                x = prices[j] - prices[i]
                if x > max:
                    max = x
        return max

