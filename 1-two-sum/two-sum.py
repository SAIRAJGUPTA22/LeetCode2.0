class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(nums):
            if target - n in res:
                return i,res[target-n]
            else:
                res[n]=i
        