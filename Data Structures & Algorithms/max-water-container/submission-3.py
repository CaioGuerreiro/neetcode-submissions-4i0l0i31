class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxWater = 0

        while left < right:
                area = (right - left) * min(heights[left], heights[right])
                maxWater = max(maxWater, area)
                if heights[left] <= heights[right]:
                        left += 1
                else:
                        right -=1
        return maxWater




"""
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

#sempre pegar o valor da menor coluna
#area = base * altura -> base = distancia entre os ponteiros  altura = heights[i]
"""
        