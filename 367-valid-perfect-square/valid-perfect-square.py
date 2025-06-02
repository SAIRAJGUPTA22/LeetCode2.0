class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        ans=1
        while left <= right:
            mid = (left+right)//2
            ans = mid*mid
            if ans == num:
                return True
            elif ans < num:
                left = mid+1
            elif mid*mid > num:
                right = mid-1
        return False
        