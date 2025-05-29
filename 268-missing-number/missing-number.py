class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n  = len(nums)
        # expected_sum = (n*(n+1))/2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum
        left = 0
        right = len(nums)-1
        nums.sort()
        while left <=right:
            mid =(left+right)//2
            if nums[mid]==  mid:
                left = mid+1
            else: 
                right = mid-1
        return left
