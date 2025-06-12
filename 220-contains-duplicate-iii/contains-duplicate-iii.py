class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        window = SortedList()
        for i in range(len(nums)):
           
            pos =window.bisect_left(nums[i]-valueDiff)
            if pos<len(window) and abs(window[pos]-nums[i])<= valueDiff:
                return True
            window.add(nums[i])
            if len(window)>indexDiff:
                window.remove(nums[i-indexDiff])
        return False