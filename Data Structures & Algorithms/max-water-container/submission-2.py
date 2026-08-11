class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxVolume = 0

        while l < r:
            lh = heights[l]
            rh = heights[r]
            volume = min(lh, rh) * (r - l)
            if volume > maxVolume:
                maxVolume = volume
            
            if lh > rh:
                r -= 1
            else:
                l += 1
        
        return maxVolume