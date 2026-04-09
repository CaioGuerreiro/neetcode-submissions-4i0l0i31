class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time O(n) space O(n) resolution
        sett = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in sett:
                lenght = 0
                while (n + lenght) in sett:
                    lenght += 1
                longest = max(longest, lenght)
        return longest

"""
 nums = [2,20,4,10,3,4,5]
                   ^   


1) Criar um set
2) verificar se n-1 tá no set ou no array
3) se não estiver é pq é o começo de uma sequencia
4) ir inteirando o numero + 1 e verificando se tá no sett
5) retorna o valor

"""

