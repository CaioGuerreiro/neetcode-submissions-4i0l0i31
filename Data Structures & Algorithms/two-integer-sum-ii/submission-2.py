class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            soma = numbers[left] + numbers[right]
            if soma > target:
                right -= 1
            elif soma < target:
                left += 1
            else:
                return[left+1, right+1]
                


"""
Input: numbers = [1,2,3,4], target = 3

[1,2,3,4]
 ^     ^

 [1,2,3,4,5] target = 8
    ^       ^
"""