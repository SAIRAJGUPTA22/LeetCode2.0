class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        left =0
        right =len(nums)-1
        max_sum =0
        while left <right:
            sum = nums[left]+nums[right]
            left +=1
            right -=1
            max_sum=max(sum,max_sum)
        return max_sum        