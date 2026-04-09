class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
                totalSum = numbers[left] + numbers[right]
                if totalSum > target:
                        right -= 1
                elif totalSum < target:
                        left += 1
                else:
                        return [left + 1, right + 1]


"""
Input: numbers = [1,2,3,4], target = 3

[2, 3, 4]
 ^     ^
 1     3
 [1,2,3,4,5] target = 8
    ^       ^
"""