class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = set(nums)
        # nums = list(nums)
        # nums.sort()
        # if len(nums)<3:
        #     return nums[-1]
        # return nums[-3]
        first = second =third = float('-inf')
        for num in nums:
            if num in(first,second,third):
                continue
            if num>first:
                first,second,third = num,first,second
                
            elif num>second:
                second,third = num,second
            elif num >third:
                third = num
        return third if third != float('-inf') else first