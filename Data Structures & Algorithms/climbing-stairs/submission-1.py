class Solution:        
    def climbStairs(self, n: int) -> int:
        """
        1: 1
        2: 1 1 | 2 - 2
        3: 1 (2 steps) | 2 (1 step)
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]