class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]


"""

Input: nums = [1,2,3,2,2]

[1,2,3,2,2]      
         f
     s
"""