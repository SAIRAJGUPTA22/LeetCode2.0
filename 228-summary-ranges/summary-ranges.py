class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(nums)
        while i <n:
            start = i
            while i+1<n and nums[i]+1 == nums[i+1]:
                i += 1
            if start ==i:
                result.append(str(nums[i]))
            else: 
                result.append('{}->{}'.format(nums[start],nums[i]))
            i += 1
        return result
