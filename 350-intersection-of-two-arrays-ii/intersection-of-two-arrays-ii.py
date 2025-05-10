class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        result = Counter(nums1)
        r=[]
        for num in nums2:
            if result[num]>0:
                r.append(num)
                result[num] -= 1
        return  r