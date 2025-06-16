class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        min_value = float('inf')
        for i in range(n-k+1):
            value = nums[i+k-1]-nums[i]
            min_value = min(min_value,value)
        return min_value
        