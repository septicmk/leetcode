class Solution(object):
    def maxProfit(self, prices):
        best, Max = 0, 0
        for i in range(len(prices)):
            cur = prices[-i-1]
            Max = max(cur,Max)
            best = max(best, Max - cur)
        return best
