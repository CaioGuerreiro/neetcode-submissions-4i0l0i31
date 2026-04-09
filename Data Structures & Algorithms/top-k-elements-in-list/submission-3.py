class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        for i in range(len(freq) -1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
"""
array nums (integer numbers)
integer k
ex: Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

bucketsort 
create dict
create freq list

populate dict
populate freq[number of time appears]

run backwards freq k times

"""
        