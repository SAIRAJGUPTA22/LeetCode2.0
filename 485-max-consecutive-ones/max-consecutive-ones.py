class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # c=0
        # i=0
        # res =[]
        # while i < len(nums):
        #     if nums[i]==1:
        #         c += 1
        #     else:
        #         res.append(c)
        #         c = 0
        #     i += 1
        # res.append(c)
        # return max(res)
        current_max = 0
        max_count = 0
        for num in nums:
            if num == 1:
                current_max += 1
            else:
                max_count=max(current_max,max_count)
                current_max =0
        max_count=max(current_max,max_count)
        return max_count
        