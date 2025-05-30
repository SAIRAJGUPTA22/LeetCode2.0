class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        # result = Counter(nums1)
        # r=[]
        # for num in nums2:
        #     if result[num]>0:
        #         r.append(num)
        #         result[num] -= 1
        # return  r
        result = Counter(nums1)
        nums2.sort()
        r=[]
        for num in set(nums2):
            left = bisect.bisect_left(nums2,num)
            if left <len(nums2) and nums2[left]==num:
                right = bisect.bisect_right(nums2,num)
                count_in_nums = right - left
                r.extend([num]*min(result[num],count_in_nums))
        return r