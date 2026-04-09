class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        sett = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left +=1 
            sett.add(s[right])
            window = (right - left) + 1
            longest = max(longest, window)

        return longest




"""
Input: s = "zxyzxyz"
Output: 3


"z x y z x y z"
 l r

set = > z, x, y,

"""













        