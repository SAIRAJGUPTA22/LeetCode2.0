class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            index = abs(i)-1
            if nums[index]>0:
                nums[index]= -nums[index]
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
        
        