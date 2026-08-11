class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1,5,2,3,4
        0,5,5,5,5
        5,4,4,4,0
        """
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        water = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]

        return water