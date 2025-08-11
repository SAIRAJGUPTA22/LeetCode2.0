class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        max_l =0
        total =  0
        window_size = 0
        nums.sort()

        for right in range(len(nums)):
            total += nums[right]
            window_size = right - left +1
            operations = window_size*(nums[right])-total
            while operations>k:
                total -= nums[left]
                left += 1
                window_size = right -left+1
                operations = window_size*(nums[right])-total
            if operations <=k:
                max_l = max(window_size,max_l)
        
        return max_l