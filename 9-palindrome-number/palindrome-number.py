class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)

        z = y[::-1]
        if y == z:
            return True
        else:
            return False

        