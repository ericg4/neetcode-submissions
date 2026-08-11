class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        lp = 0
        rp = len(heights) - 1

        while lp < rp:
            area = min(heights[lp], heights[rp]) * (rp - lp)

            if area > maxWater:
                maxWater = area
            
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        
        return maxWater