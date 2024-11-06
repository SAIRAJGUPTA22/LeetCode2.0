class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=str(x)
        z=list(y)
        w=[]
        for i in range(len(z)-1,-1,-1):
            w.append(z[i])
        w = ''.join(w)

        return w==y
        