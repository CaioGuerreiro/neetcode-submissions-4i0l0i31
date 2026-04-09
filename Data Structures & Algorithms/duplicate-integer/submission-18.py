class Solution:

        def hasDuplicate(self, nums: list[int]) -> bool:
                sett = set()

                for n in nums:
                        if n in sett:
                                return True
                        sett.add(n)
                return False

    