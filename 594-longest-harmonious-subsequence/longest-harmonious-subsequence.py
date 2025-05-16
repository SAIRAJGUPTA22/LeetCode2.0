class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        max_count =0
        current_count =0
        for num in nums:
            if num+1 in c:
                current_count = c[num]+c[num+1]
                max_count=max(max_count,current_count)
        return max_count