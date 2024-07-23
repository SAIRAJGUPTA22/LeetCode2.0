class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        low = 0
        while low<=n:
            x = (low+n)//2
            if target == nums[x]:
                return x
            if nums[x]<target:
                low = x+1
            else:
                n=x-1
        return low