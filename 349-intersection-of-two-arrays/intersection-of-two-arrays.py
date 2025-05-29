class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return list(set(nums1)&set(nums2))
        def binary_search(arr,target):
            left =0
            right = len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid]== target:
                    return True
                if arr[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return False
        nums1_unique = list(set(nums1))
        nums2.sort()
        result =[]
        for num in nums1_unique:
            if binary_search(nums2,num):
                result.append(num)
        return result