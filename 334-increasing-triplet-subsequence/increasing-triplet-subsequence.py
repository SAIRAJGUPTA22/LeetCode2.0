class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        small = float('inf')
        small2 = float('inf')
        for i in nums:
            if i <= small:
                small = i
            elif i <= small2:
                small2 = i
            else:
                return True
        return False
        