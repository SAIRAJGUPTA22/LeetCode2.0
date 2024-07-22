class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        left = 0
        n = len(s)
        sub = set()

        for right in range(n):
            if s[right] not in sub:
                sub.add(s[right])
                maxlength=max(maxlength,right-left+1)
            else:
                while s[right] in sub:
                    sub.remove(s[left])
                    left += 1
                sub.add(s[right])
        return maxlength


        