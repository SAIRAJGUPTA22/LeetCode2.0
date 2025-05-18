class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = Counter(nums)
        res=[]
        for i in n:
            if n[i]==2:
                res.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res