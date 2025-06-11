class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length =0
        r =set()
        for right in range(len(s)):
            while s[right] in r:
                r.remove(s[left])
                left +=1
            r.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length
        