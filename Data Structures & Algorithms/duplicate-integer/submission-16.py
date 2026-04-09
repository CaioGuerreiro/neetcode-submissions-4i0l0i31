class Solution:

        def hasDuplicate(self, nums: list[int]) -> bool:
                sett = set()

                for i in range(len(nums)):
                        if nums[i] in sett:
                                return True
                        
                        sett.add(nums[i])
                
                return False

    