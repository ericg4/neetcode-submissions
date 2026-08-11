class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 2}
        
    def climbStairs(self, n: int) -> int:
        """
        1: 1
        2: 1 1 | 2 - 2
        3: 1 (2 steps) | 2 (1 step)
        """
        if n in self.memo:
            return self.memo[n]

        oneStepDown = self.climbStairs(n - 1)        
        twoStepsDown = self.climbStairs(n - 2)

        val = oneStepDown + twoStepsDown
        if n not in self.memo:
            self.memo[n] = val
        return val