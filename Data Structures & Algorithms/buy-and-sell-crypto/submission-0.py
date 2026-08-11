class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        10,3,5,6,7,1,10
                   l r
        """
        n = len(prices)

        if n == 1:
            return 0

        l = 0
        r = 1

        maxProfit = 0

        while r < n:
            if prices[r] <= prices[l]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        
        return maxProfit