class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = Counter(s)
        max_length = 0
        has_odd = False
        for c in m.values():
            max_length += (c//2)*2
            if c%2 !=0:
                has_odd = True
        if has_odd ==True:
            max_length += 1
        return max_length
        
        