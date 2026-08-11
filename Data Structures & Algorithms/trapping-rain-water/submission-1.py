class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1,5,2,3,4
        0,0,5,5,5
        5,4,4,4,0
        """
        n = len(height)

        lMax = [0] * n
        rMax = [0] * n

        lMax[0] = height[0]
        for i in range(1, n):
            lMax[i] = max(lMax[i - 1], height[i])
        
        rMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rMax[i] = max(rMax[i + 1], height[i])
        
        maxWater = 0
        for i in range(n):
            maxWater += min(lMax[i], rMax[i]) - height[i]
        
        return maxWater