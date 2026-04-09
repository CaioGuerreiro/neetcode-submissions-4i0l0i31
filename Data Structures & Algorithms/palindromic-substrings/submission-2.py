class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 

        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >=0 and right <len(s) and s[left]==s[right]:
                res += 1
                left -= 1
                right += 1
            # even lengt
            left, right = i, 1+i
            while left >=0 and right <len(s) and s[left]==s[right]:
                res += 1
                left -= 1
                right += 1 

        return res