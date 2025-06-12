class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a = set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            a.add(nums[i])
            if len(a)>k:
                a.remove(nums[i-k])
        return False