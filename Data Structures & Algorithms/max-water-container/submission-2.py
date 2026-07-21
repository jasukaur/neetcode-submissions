class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1

        maxWater = float("-inf")

        while l < r:
            wd = (r-l)
            ht = min(heights[l], heights[r])

            maxWater = max(maxWater, ht*wd)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l+=1
        
        return maxWater