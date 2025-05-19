class Solution(object):
    def calPoints(self, nums):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for i in range(len(nums)):
            if nums[i] == 'C' and i>0:
                result.pop(-1)
            elif nums[i] == 'D' and i>0:
                result.append(result[-1]*2)
            elif nums[i] == '+' and i>0:
                result.append(result[-1]+result[-2])
            else:
                result.append(int(nums[i]))
        return sum(result[::])
        