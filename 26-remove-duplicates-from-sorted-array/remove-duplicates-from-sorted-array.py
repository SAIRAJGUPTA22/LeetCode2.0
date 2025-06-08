class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # """
        # k= 1
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[k] = nums[i]
        #         k = k+1
        # for i in range(k,len(nums)):
        #     nums[i] ='_'
        # return k

        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k = k+1
        for i in range(k,len(nums)):
            nums[i] ="_"
        return k