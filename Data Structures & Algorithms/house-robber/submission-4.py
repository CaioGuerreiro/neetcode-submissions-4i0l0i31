class Solution:
        def rob(self, nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            # time O(n) space O(1)
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
"""
Input: nums = [1,1,3,3]
                 

temp = 1
rob1 = 0
rob2 = 0
             
"""