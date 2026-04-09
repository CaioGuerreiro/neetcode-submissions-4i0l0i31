class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

"""
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output:     [["hat"],["act", "cat"],["stop", "pots", "tops"]]


[0, 1, 0, 0, 0, 0,... 0, 0, ... 0]
[1, 0, 1, 0, 0, 0,... 1, 0, ... 0]
"""