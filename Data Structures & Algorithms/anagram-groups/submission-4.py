class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())



        # complexidade de tempo = O(n * m)
        # complexidade de espaço = 0(n)


"""
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

[1, 0, 1... 1 ...0]


"""