class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxWindow = 0
        sett = set()
#Input: s="pwwkew"
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            window = (right - left) + 1
            maxWindow = max(maxWindow, window)
        return maxWindow

        