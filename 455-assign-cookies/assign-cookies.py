class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        num_child = len(g)
        num_cookies = len(s)
        child_ptr=cookie_ptr =0
        while child_ptr<num_child and cookie_ptr <num_cookies:
            if s[cookie_ptr]>=g[child_ptr]:
                child_ptr += 1
            cookie_ptr += 1
        return child_ptr