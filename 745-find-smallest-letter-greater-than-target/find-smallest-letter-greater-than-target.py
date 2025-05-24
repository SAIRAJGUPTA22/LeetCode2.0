class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # c = ord(target)
        # let = [ord(i) for i in letters]
        # for i in range(len(let)):
        #     if let[i] >c:
        #         return letters[i]
        # return letters[0]
        c = bisect.bisect_right(letters,target)
        return letters[c] if c<len(letters) else letters[0]