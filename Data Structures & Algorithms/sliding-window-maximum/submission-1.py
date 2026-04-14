class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left, right = 0 , 0
        queue = deque()

        while right < len(nums):
                while queue and nums[queue[-1]] < nums[right]:
                        queue.pop()
                queue.append(right)
                if left > queue[0]:
                        queue.popleft()
                if (right + 1) >= k:
                        output.append(nums[queue[0]])
                        left += 1
                right += 1
        return output

"""
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]



1. create a queue
2. if nums[i] greater than queue right most. popleft() and add nums[i]
   else add nums[i]
3. save the max value of queue
4. shift the window

"""