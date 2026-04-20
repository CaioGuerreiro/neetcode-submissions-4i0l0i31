class Solution:
    def scoreOfString(self, s: str) -> int:
        sumString = 0
        for i in range(len(s)- 1):
            sumString += abs(ord(s[i]) - ord(s[i+1]))
        
        return sumString

"""
c = 99
o = 111
d = 100
e = 101
"""