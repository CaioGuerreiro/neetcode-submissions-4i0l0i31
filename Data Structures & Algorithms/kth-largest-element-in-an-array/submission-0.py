class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        res = []
        while len(nums) > k: 
            heapq.heappop(nums)
        return nums[0]
            
    

#Input: nums = [2,3,1,5,4] k = 2
"""
[2,3,1,5,4]
[-2,-3,-1,-5,-4]

[-5, -4, -3, -2, -1]
                    4
                   / \
                  2   3
                 / 
                1   

"""
       