class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        sett = set()
        longest = 0

#       s="d v d f"
#              l
#                r
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
                
            
            sett.add(s[right])
            window = (right - left) + 1
            longest = max(longest, window)
        return longest

        