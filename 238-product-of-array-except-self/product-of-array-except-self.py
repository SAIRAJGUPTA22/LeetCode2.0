class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        for i in range(n-2,-1,-1):
            a[i]=a[i+1]*nums[i+1]
        b=1
        for j in range(1,n):
            b = b*nums[j-1]
            a[j]=a[j]*b
        return a
