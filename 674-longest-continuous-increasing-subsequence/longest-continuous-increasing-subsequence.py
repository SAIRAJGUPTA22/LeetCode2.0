class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        max_c =0
        for i in range(len(nums)):
            if (i<len(nums)-1) and nums[i+1]>nums[i]:
                c += 1
            else:
                max_c = max(max_c,c)
                c = 0
        max_c = max(max_c,c)
        return max_c+1
        