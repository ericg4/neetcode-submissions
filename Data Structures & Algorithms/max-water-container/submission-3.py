class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxVol = 0

        while l < r:
            lHeight = heights[l]
            rHeight = heights[r]

            volume = min(lHeight, rHeight) * (r - l)

            if volume > maxVol:
                maxVol = volume
            
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
        
        return maxVol