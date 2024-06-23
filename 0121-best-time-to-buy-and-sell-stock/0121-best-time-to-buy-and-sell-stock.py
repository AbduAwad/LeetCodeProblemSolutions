class Solution(object):
    def maxProfit(self, prices):
        
        right, left, maxProfit = 1,0,0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            right += 1
        return maxProfit
            