class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1])
        result = sign * rev
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result