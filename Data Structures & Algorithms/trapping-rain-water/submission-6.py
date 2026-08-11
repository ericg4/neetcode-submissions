class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0

        leftMaxes = [0] * len(height)
        rightMaxes = [0] * len(height)

        for i in range(1, len(height)):
            leftMaxes[i] = max(leftMaxes[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            rightMaxes[i] = max(rightMaxes[i + 1], height[i + 1])

        for i, val in enumerate(height):
            volume += max(0, min(leftMaxes[i], rightMaxes[i]) - val)
        
        return volume