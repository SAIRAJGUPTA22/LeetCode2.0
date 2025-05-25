class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = max(nums)
        # c=0
        # for num in nums:
        #     if num <>n:
        #         if n>= 2*num:
        #             c=c+1
        # if c == len(nums)-1:
        #     return nums.index(n)
        # return -1

        # max_val = -1
        # second_max = -1
        # index = -1

        # for i,n in enumerate(nums):
        #     if n>max_val:
        #         second_max = max_val
        #         max_val = n
        #         index = i
        #     elif n>second_max:
        #         second_max = n
        # if max_val >= 2*second_max:
        #     return index
        # return -1

        n=sorted(nums)
        maximum = max(nums)
        if n[-1]>=n[-2]*2:
            return nums.index(maximum)
        return -1


        