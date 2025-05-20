class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s=''.join(str(ord(ch)-ord('a')+1) for ch in s)

        for _ in range(k):
            s = str(sum(int(digit) for digit in s))
        return int(s)