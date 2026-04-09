class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #time O(n) space O(n)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


"""
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
[30,38,30,36,35,40,28]
        ^  ^

res = []

"""