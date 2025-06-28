class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_l = 0
        total = 0
        wiondow_size =0

        nums.sort()

        for right in range(len(nums)):
            total += nums[right]

            window_size = right - left +1
            operations = window_size * nums[right] - total

            while operations >k:
                total -= nums[left]
                left = left+1
                window_size = right - left +1
                operations = window_size*nums[right] - total
            if operations <=k:
                max_l = max(max_l,window_size)
        return max_l
