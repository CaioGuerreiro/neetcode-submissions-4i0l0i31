class Solution:

        def hasDuplicate(self, nums: list[int]) -> bool:
                sett = set()

                for i in range(len(nums)): # tc O(n) sc O(n)
                                           # tc O(n long n) sc O(1)
                        if nums[i] in sett:
                                return True
                        
                        sett.add(nums[i])
                
                return False

    