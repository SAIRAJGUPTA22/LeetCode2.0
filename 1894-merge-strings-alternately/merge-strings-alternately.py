class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        a = len(word1)
        b = len(word2)
        c= max(a,b)
        i=0
        while i <=c:
            if i <a:
                result.append(word1[i])
            if i <b:
                result.append(word2[i])
            i =i+1
        return ''.join(result)