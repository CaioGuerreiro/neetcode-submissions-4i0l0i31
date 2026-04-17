class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # time O(log n) space O(1)
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            # target na esquerda
            # [4, 5, 6, 7, 0, 1, 2] = 5
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
