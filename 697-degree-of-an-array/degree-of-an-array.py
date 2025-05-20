class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        left ={}
        right ={}
        frequency =defaultdict(int)
        for i,num in enumerate(nums):
            if num not in left:
                left[num]=i
            right[num] = i
            frequency[num] +=1
        max_v = max(frequency.values())
        min_len = len(nums)
        for num in frequency:
            if frequency[num] == max_v:
                min_len=min(min_len,right[num]-left[num] +1)
        return min_len
