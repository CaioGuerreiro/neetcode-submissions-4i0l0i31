class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right)//2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            print(res)
        return res
#                |    
#       [3,4,5,6,1,2]
#              l   r
#            |
#       [4,5,6,1,2,3]
#              l   r
        