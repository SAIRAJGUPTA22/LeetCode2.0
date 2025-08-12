class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        total = 0
        max_l = 0
        window_size = 0
        nums.sort()


        for right in range(len(nums)):
            window_size = right - left +1
            total += nums[right]
            operations = nums[right]*window_size - total

            while operations >k:
                total -= nums[left]
                left +=1
                window_size = right -left+1
                operations = (nums[right]*window_size) - total
            if operations <=k:
                max_l = max(max_l,right-left+1)
        return max_l
