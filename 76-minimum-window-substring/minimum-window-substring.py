class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        

        t_freq = Counter(t)
        window_freq ={}
        left = 0
        min_len = float('inf')
        min_left = 0
        formed = 0
        req = len(t_freq)

        for right,char in enumerate(s):
            window_freq[char] = window_freq.get(char,0)+1
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed +=1
            while formed == req:
                window_size = right-left+1
                if window_size < min_len:
                    min_len = window_size
                    min_left = left
                left_char = s[left]
                window_freq[left_char] -= 1
                if left_char in t_freq and window_freq[left_char]<t_freq[left_char]:
                    formed -=1
                left +=1
        return "" if min_len == float('inf') else s[min_left:min_left+min_len]
        