class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
"""
Input: s = "racecar", t = "carrace"
Output: true

s.sort() # O(n logn)
t.sort() # O(n logn)

loop # O(n)
if s != t - > False  -> True

complexidade tempo O(n log n)
complexidade space O(1)

complexidade time O(n)
complexidade space O(1)

s = "racecar", t = "carrace"
     ^   
"""
          

