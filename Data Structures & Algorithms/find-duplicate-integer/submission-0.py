class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


"""

Input: nums = [1,2,3,2,2]

[1,2,3,2,2]      
         f
     s
"""