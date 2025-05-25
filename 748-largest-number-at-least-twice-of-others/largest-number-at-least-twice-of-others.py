class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        c=0
        for num in nums:
            if num <>n:
                if n>= 2*num:
                    c=c+1
        if c == len(nums)-1:
            return nums.index(n)
        return -1
        