class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        totalLen = len(merged)
        print(totalLen //2 -1)
        print(totalLen//2)
        print((merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
        else:
            return merged[totalLen // 2]
"""
Input: nums1 = [1,3], nums2 = [2,4]
            [1, 2, 3, 4]
         merged[4 // 2 - 1 ]
"""
