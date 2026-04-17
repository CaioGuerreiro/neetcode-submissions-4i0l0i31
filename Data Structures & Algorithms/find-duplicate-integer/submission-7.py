class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()

        for n in range(len(nums)):
            if nums[n] in sett:
                return nums[n]
            sett.add(nums[n])
           
        
        