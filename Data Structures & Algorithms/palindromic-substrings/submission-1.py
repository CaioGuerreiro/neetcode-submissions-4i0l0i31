class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 

        for i in range(len(s)):
            for j in range(i, len(s)):
                left, right = i, j
                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1
                res += (left >= right)
        
        return res