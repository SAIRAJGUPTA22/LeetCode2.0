class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_freq = Counter(t)
        left = 0
        window={}
        formed = 0
        req=len(t_freq)
        min_length= float('inf')

        for right,n in enumerate(s):
            window[n] = window.get(n,0)+1

            if n in t_freq and window[n]==t_freq[n]:
                formed += 1
            while formed == req:
                window_size = right - left +1
                if window_size < min_length:
                    min_length = min(min_length,window_size)
                    min_left = left 
                left_char = s[left]
                window[left_char] = window.get(left_char,0)-1
                if left_char in t_freq and window[left_char]<t_freq[left_char]:
                    formed -= 1
                left +=1

        return "" if min_length == float('inf') else s[min_left:min_left+min_length] 



        

        