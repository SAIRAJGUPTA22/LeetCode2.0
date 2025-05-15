class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        l = sorted(score, reverse=True)
        s = {score:i+1 for i,score in enumerate(l)}
        res =[]
        for m in score:
            po=s[m]
            if po==1:
                res.append('Gold Medal')
            elif po==2:
                res.append('Silver Medal')
            elif po==3:
                res.append('Bronze Medal')
            else:
                res.append(str(po))
        return res