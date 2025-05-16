class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        c = n/2
        l = Counter(candyType)
        if c<len(l):
            return c
        else:
            return len(l)
        