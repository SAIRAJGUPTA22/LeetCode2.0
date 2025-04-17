class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        S= s.strip().split(" ")
        r = len(S[-1])
        return r
        