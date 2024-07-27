class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x1= str(x)
        x2=list(x1)
        l=[]
        s=len(x2)-1

        for i in range(len(x2)-1,-1,-1):
            l.append((x2[i]))
        l =''.join(l)

        return l==x1

        