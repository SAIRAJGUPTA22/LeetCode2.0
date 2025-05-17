class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums,reverse=True)
        res = max(n[0]*n[1]*n[2],n[-1] * n[-2] * n[0])
        return res