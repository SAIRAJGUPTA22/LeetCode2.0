class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=1
        max_c =1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c += 1
            else:
                max_c = max(max_c,c)
                c = 1
        max_c = max(max_c,c)
        return max_c
        