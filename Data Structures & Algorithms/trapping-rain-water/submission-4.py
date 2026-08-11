class Solution:
    def trap(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1

        leftMax = height[lp]
        rightMax = height[rp]

        water = 0

        while lp < rp: 
            if leftMax < rightMax:
                lp += 1
                leftMax = max(leftMax, height[lp])
                water += leftMax - height[lp]
            else:
                rp -= 1
                rightMax = max(rightMax, height[rp])
                water += rightMax - height[rp]
        
        return water