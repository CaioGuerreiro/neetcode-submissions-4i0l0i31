class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
"""
Input: nums = [3,4,5,6], target = 7
Output: [0,1]


[3,4,5,6] == target

Brute Force
loop
    loop
        if soma == target
            return True

complexidade tempo O(n^2)
complexidade de espaço O(1)

enumerate
nums = [3,4,5,6], target = 7
diff = 7 - 4




"""