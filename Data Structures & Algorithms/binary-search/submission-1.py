class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

      
"""
Input: nums = [-1,0,2,4,6,8], target = 4

nlogn













$0
[-1,0,2,4,6,8]
      m l    r
"""
        