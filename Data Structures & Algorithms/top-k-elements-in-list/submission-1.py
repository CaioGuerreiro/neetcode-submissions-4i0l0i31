class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time O(n) space O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
"""
1) criar freq do tamanho de n+1 e dicionario
2) popular o dicionario
3) o index de freq é a qtd de vzs q o num aparece
4) percorre res pegando os mais freq
"""