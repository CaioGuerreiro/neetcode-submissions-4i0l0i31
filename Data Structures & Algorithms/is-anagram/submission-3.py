class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
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
          

