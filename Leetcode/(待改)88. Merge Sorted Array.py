class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        new_nums1 = []
        for i in nums1:
            if i != 0:
                new_nums1.append(i)
        if len(nums1) >= m+n :
            final = new_nums1 + nums2
            final.sort()
            return final
        
